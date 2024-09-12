from django.urls import path
from ecommerce import views

urlpatterns=[
    path('signup',views.signup1,name='signup'),
    path('login',views.login1,name='login'),
    path('',views.main,name='main'),
    path('logout1/',views.logout1,name='logout1'),
    path('catagory',views.catagory1,name='catagory'),
    path('collection/<str:name>',views.collections,name='collection'),
    path('product/<str:name>',views.product,name='product'),
    path('add_cart/<int:use>/<int:pro>',views.add_cart,name='add_cart'),
]



