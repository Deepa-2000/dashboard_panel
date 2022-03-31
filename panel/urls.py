from django.urls import path
from . import views
from . import views_product

urlpatterns = [
    path('',views.login, name= 'login'),
    path('login/', views.login, name= 'login'),
    path('logout/', views.logout,name='logout'),
    path('register/', views.register, name= 'register'),
    path('dashboard/', views.dashboard, name= 'dashboard'),
    path('orders_tables/',views.orders, name='orders'),
    path('orders_form/',views.ordersform, name='ordersform'),
    path('orders_edit/<int:id>',views.ordersedit, name='ordersedit'),
    path('orders_update/<int:id>',views.ordersupdate,name='ordersupdate'),
    path('orders_delete/<int:id>',views.ordersdelete, name='ordersdelete'),
    path('products_tables/',views_product.products, name='products'),
    # path('products_form/',views_product.productsform, name='productsform'),
    path('banners_tables/',views.banners, name='banners'),

]
