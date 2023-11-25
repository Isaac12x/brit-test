from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Cart, Item

# example of a Class Based View (CBV)
class ProtectedView(LoginRequiredMixin, TemplateView):
    template_name = 'pages/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['items'] = Item.objects.all()
        return context


# example of a Function Based View
def cart_detail(request):
    user_cart, created = Cart.objects.get_or_create(user=request.user)
    return render(request, 'pages/cart_detail.html', {'cart': user_cart})


