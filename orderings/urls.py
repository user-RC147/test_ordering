from django.urls import path
from . import views

app_name='orderings'

urlpatterns = [
    path('',views.IndexPage.as_view(), name='index'),
    path('order', views.OrderListPage.as_view(), name='order_page'),
    path('create-order/', views.CreateOrderPage.as_view(), name='create_order'),
    path('create-product/',views.CreateProductPage.as_view(), name='create_product'),
    path('create-client/',views.CreateClientPage.as_view(), name='create_client'),
    path('orders/<pk>/',views.OrderDetailPage.as_view(),name='order_detail')
]
