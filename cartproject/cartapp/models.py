from django.db import models
from django.urls import reverse

# Create your models here.
class Category(models.Model):
    name=models.CharField(max_length=250)
    slug=models.SlugField(max_length=250)
    img=models.ImageField(upload_to='category')
    desc=models.TextField()

    class Meta:
        ordering=('name',)
        verbose_name='category'
        verbose_name_plural='categories'

    def get_url(self):
        return reverse('cartapp:probycat',args=[self.slug])

    def __str__(self):
        return '{}'.format(self.name)

class Product(models.Model):
    name=models.CharField(max_length=250)
    slug=models.SlugField(max_length=250)
    price=models.DecimalField(max_digits=10,decimal_places=2)
    img=models.ImageField(upload_to='products')
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    desc=models.TextField()
    stock=models.IntegerField()
    available=models.BooleanField()
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)

    def get_url(self):
        return reverse('cartapp:prodet',args=[self.category.slug,self.slug])

    class Meta:
        ordering=('name',)
        verbose_name='product'
        verbose_name_plural='products'

    def __str__(self):
        return '{}'.format(self.name)