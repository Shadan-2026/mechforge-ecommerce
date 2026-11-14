import stripe
from django.conf import settings
from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.cache import never_cache # 1. Import the cache tool
from .models import Product

stripe.api_key = settings.STRIPE_SECRET_KEY

# 2. Add the @never_cache decorator above your views
@never_cache
def store_view(request):
    products = Product.objects.all()
    cart = request.session.get('cart', {})
    cart_count = sum(cart.values())
    return render(request, 'store/store.html', {'products': products, 'cart_count': cart_count})

@never_cache
def product_detail(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    cart = request.session.get('cart', {})
    cart_count = sum(cart.values())
    return render(request, 'store/product.html', {'product': product, 'cart_count': cart_count})

def add_to_cart(request, product_id):
    product_id = str(product_id) 
    cart = request.session.get('cart', {})
    
    if product_id in cart:
        cart[product_id] += 1
    else:
        cart[product_id] = 1
        
    request.session['cart'] = cart
    return redirect('cart_view')

@never_cache
def cart_view(request):
    cart = request.session.get('cart', {})
    cart_items = []
    cart_total = 0
    
    for product_id, quantity in cart.items():
        product = get_object_or_404(Product, id=int(product_id))
        total_price = product.price * quantity
        cart_total += total_price
        cart_items.append({'product': product, 'quantity': quantity, 'total_price': total_price})
    
    cart_count = sum(cart.values())
    return render(request, 'store/cart.html', {'cart_items': cart_items, 'cart_total': cart_total, 'cart_count': cart_count})

def checkout(request):
    cart = request.session.get('cart', {})
    if not cart:
        return redirect('store')

    line_items = []
    for product_id, quantity in cart.items():
        product = get_object_or_404(Product, id=int(product_id))
        line_items.append({
            'price_data': {
                'currency': 'inr',
                'product_data': {'name': product.name},
                'unit_amount': int(product.price * 100), 
            },
            'quantity': quantity,
        })
    
    checkout_session = stripe.checkout.Session.create(
        line_items=line_items,
        mode='payment',
        success_url='http://127.0.0.1:8000/success/',
        cancel_url='http://127.0.0.1:8000/cancel/',
    )
    return redirect(checkout_session.url)

def success_view(request):
    if 'cart' in request.session:
        del request.session['cart']
    return render(request, 'store/success.html')

def cancel_view(request):
    return render(request, 'store/cancel.html')