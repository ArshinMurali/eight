from . models import Cart,Cart_item
from . views import cartinte_id

def counter (request):
    item_count=0
    if 'admin' in request.path:
        return {}
    else:
        try:
            cart=Cart.objects.filter(cart_id=cartinte_id(request))
            cart_items=Cart_item.objects.all().filter(cart=cart[:1])
            for cart_item in cart_items:
                item_count += cart_item.quantity
        except Cart.DoesNotExist:
            item_count=0
    return dict(item_count=item_count)