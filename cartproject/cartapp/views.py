from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from . models import Category,Product
from django.core.paginator import Paginator,EmptyPage,InvalidPage
def Allpc(request,cslug=None):
    cpage=None
    products=None
    if cslug != None:
        cpage= get_object_or_404(Category,slug=cslug)
        products=Product.objects.all().filter(category=cpage,available=True)
    else:
        products=Product.objects.all().filter(available=True)

    paginator=Paginator(products,3)
    try:
        page=int(request.GET.get('page','1'))
    except:
        page=1
    try :
        pro_page=paginator.page(page)
    except (EmptyPage, InvalidPage):
        pro_page=paginator.page(paginator.num_pages)

    return render(request,'category.html',{'category':cpage,'products':pro_page})

def prodet(request,cslug,pslug):
    product=Product.objects.get(category__slug=cslug,slug=pslug)
    return render(request,'product.html',{'product':product})
