from django.shortcuts import render, reverse, redirect
from django.contrib import messages

from .forms import OrderForm

# Create your views here.
def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "There's nothing in your bag at the moment" )
        return redirect(reverse('products'))
    
    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51SBIWjFnNv9Vq3ftQJc2uFRQPP0fURiI206RWyGDQFXVdYVRkG5Lul1oZ1hpba8P4CT8dx8Xh7MoDILE2mSsi9Ds00btmaPVkY',
        'client_secret': 'test client secret',

    }

    return render(request, template, context)