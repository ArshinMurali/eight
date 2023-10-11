from django.db import models
from cartapp.models import Product

class Cart(models.Model):
    cart_id=models.CharField(max_length=250,blank=True)
    date_added=models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table='Cart'
        ordering=['date_added',]

    def __str__(self):
        return '{}'.format(self.cart_id)

class Cart_item(models.Model):
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    cart=models.ForeignKey(Cart,on_delete=models.CASCADE)
    quantity=models.IntegerField()
    active=models.BooleanField(default=True)

    class Meta:
        db_table='Cart_item'
    def total(self):
        return self.product.price * self.quantity

    def __str__(self):
        return '{}'.format(self.product)