from django.shortcuts import render, redirect, get_object_or_404
from cartapp.models import Product
from . models import Cart,Cart_item
from django.core.exceptions import ObjectDoesNotExist
def cartinte_id(request):
    cart=request.session.session_key
    if not cart:
        cart=request.session.create()
    return cart

def adding_cart(request,product_id):
    product=Product.objects.get(id=product_id)
    try:
        cart=Cart.objects.get(cart_id=cartinte_id(request))
    except Cart.DoesNotExist:
        cart=Cart.objects.create(cart_id=cartinte_id(request))
        cart.save(),
    try:
        cart_item=Cart_item.objects.get(product=product, cart=cart)
        if cart_item.quantity < cart_item.product.stock:
            cart_item.quantity += 1
            cart_item.save()
    except Cart_item.DoesNotExist:
        cart_item=Cart_item.objects.create(product=product,quantity=1,cart=cart)
        cart_item.save()
    return redirect("addcart:cart_detail")
def cart_detail(request,total=0, counter=0, cart_items=None):
    try:
        cart=Cart.objects.get(cart_id=cartinte_id(request))
        cart_items=Cart_item.objects.filter(cart=cart, active=True)
        for carts in cart_items:
            total += (carts.product.price * carts.quantity)
            counter += carts.quantity
    except ObjectDoesNotExist:
        pass
    return render(request,'cart.html',dict(cart_items=cart_items,total=total,counter=counter))

def cart_remove(request,product_id):
    cart=Cart.objects.get(cart_id=cartinte_id(request))
    product=get_object_or_404(Product,id=product_id)
    cart_item=Cart_item.objects.get(product=product,cart=cart)
    if cart_item.quantity > 1:
        cart_item.quantity -= 1
        cart_item.save()
    else:
        cart_item.delete()
    return redirect('addcart:cart_detail')

def full_delete(request,product_id):
    cart=Cart.objects.get(cart_id=cartinte_id(request))
    product=get_object_or_404(Product,id=product_id)
    cart_item=Cart_item.objects.get(product=product,cart=cart)
    cart_item.delete()
    return redirect('addcart:cart_detail')





