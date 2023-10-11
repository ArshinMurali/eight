from . import views
from django.urls import path
app_name='cartapp'
urlpatterns = [

    path('', views.Allpc, name='Allpc'),
    path('<slug:cslug>/', views.Allpc, name='probycat'),
    path('<slug:cslug>/<slug:pslug>/', views.prodet, name='prodet'),
]

