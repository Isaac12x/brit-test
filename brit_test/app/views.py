from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt

# example of a Class Based View (CBV)
class ItemsView(LoginRequiredMixin, TemplateView):
    template_name = 'pages/items.html'

    def get_context_data(self, **kwargs):
        from .models import Item
        context = super().get_context_data(**kwargs)
        context['items'] = Item.objects.all()
        return context


#example of a Function Based View
@login_required(login_url='/accounts/login/')
def summary(request):
    from .models import Cart
    user_cart, created = Cart.objects.get_or_create(user=request.user)
    return render(request, 'pages/summary.html', {'cart': user_cart, 'items': user_cart.cart_items.all(), 'total_amount': user_cart.total_amount})

@login_required(login_url='/accounts/login/')
@csrf_exempt  #temporary
def add_to_summary(request):
    from .models import Cart, Item
    if request.method != 'POST':
        return JsonResponse({'status': 'error'}, status=400)

    user_cart, created = Cart.objects.get_or_create(user=request.user)
    
    try:
        item = Item.objects.get(pk=request.POST.get('item')) 
        new_item, created = user_cart.cart_items.get_or_create(item=item)
        breakpoint()
        if not created:
            new_item.quantity += 1
            new_item.save()
        else:
            user_cart.cart_items.add(new_item)
        return JsonResponse({'success': True})
    except Exception as e:  #wrong! the way to do it is with specific exceptions
        return JsonResponse({'success': False, 'error': str(e)})
