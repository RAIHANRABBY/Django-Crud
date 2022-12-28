from django.urls import path
from . import views
urlpatterns = [

    path('product/', views.create_product, name='product-create'),
    path('',views.productView,name='Product-view'),
    path('home/',views.productView,name='Product-view'),
    path('update/<str:pk>/',views.productUpdate,name='product-update'),
    path('delete/<str:pk>/',views.productDelete,name='product-delete'),

]   
