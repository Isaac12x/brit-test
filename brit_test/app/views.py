from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required

# example of a Class Based View (CBV)
class ItemsView(LoginRequiredMixin, TemplateView):
    template_name = 'pages/home.html'

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
    return render(request, 'pages/summary.html', {'cart': user_cart})

@login_required(login_url='/accounts/login/')
def add_to_summary(request):
    from .models import Cart, Item
    user_cart, created = Cart.objects.get_or_create(user=request.user)
    
    try:
        item = Item.objects.get(pk=request.GET.get('item')) 
        user_cart.items.add(item)
        return JsonResponse({'success': True})
    except Exception as e:  #wrong! the way to do it is with specific exceptions
        return JsonResponse({'success': False, 'error': str(e)})
