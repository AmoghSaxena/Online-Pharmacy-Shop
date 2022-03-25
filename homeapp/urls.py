from django.urls import path
from .import views

urlpatterns=[
    path('',views.index,name='index'),
    path('index', views.index, name='index'),
    path('login', views.login,name='login'),
    path('registration',views.register, name='register'),
    path('blog',views.blog,name='index'),
    path('cart',views.cart,name='index'),
    path('category',views.category,name='index'),
    path('checkout',views.checkout,name='index'),
    path('confirmation',views.confirmation,name='index'),
    path('contact',views.contact,name='index'),
    path('elements',views.elements,name='index'),
    path('singleblog',views.singleblog,name='index'),
    path('singleblog2',views.singleblog2,name='index'),
    path('singleblog3',views.singleblog3,name='index'),
    path('singleblog4',views.singleblog4,name='index'),
    path('singleblog5',views.singleblog5,name='index'),
    path('singleproduct',views.singleproduct,name='index'),
    path('tracking',views.tracking,name='index'),
    path('tandc',views.tandc,name='tandc'),
    path('inputreg', views.inputreg, name='inputreg'),
    path('checkrno',views.checkrno,name='checkrno'),
    path('newsletter', views.inputreg, name='newsletter'),
]