from django.urls import path,include
from .views import ProductList,ProductDetail

app_name = "api"

urlpatterns = [
    path('',ProductList.as_view(),name="productslist"),
    path('product/<str:pk>/',ProductDetail.as_view(),name="productsdetail"),
    path('api-auth/', include('rest_framework.urls')),
]