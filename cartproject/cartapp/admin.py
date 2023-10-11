from django.contrib import admin
from . models import Category,Product
# Register your models here.
class Cadmin(admin.ModelAdmin):
    list_display = ['name','slug','img','desc']
    prepopulated_fields = {'slug':('name',)}
admin.site.register(Category,Cadmin)

class Padmin(admin.ModelAdmin):
    list_display = ['name','img','desc','slug','available','stock','price','created','updated']
    list_editable = ['available','stock','price']
    prepopulated_fields = {'slug':('name',)}
admin.site.register(Product,Padmin)
