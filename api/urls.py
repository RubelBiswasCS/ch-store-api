from django.urls import path,include
from .views import (
    ProductList,
    ProductDetail,
    CartList,
    CartDetail,
    AddressList,
    OrderList,
    BlacklistTokenUpdateView
    )

from users.views import MyTokenObtainPairView,TokenRefreshView
app_name = "api"

urlpatterns = [
    path('user/',include('users.urls',namespace='users')),
    path('api-auth/', include('rest_framework.urls')),
    path('',ProductList.as_view(),name="productslist"),
    path('product/<str:pk>/',ProductDetail.as_view(),name="productsdetail"),
    path('cart/',CartList.as_view(),name="cartlist"),
    # path('cart/create/', CartCreate.as_view(),name="cartcreate"),
    path('cart/<str:pk>/',CartDetail.as_view(),name="cartdetail"),
    path('user/address/', AddressList.as_view(),name="addresslist"),
    path('placeorder/',OrderList.as_view(),name="placeorder"),
    path('getorder/',OrderList.as_view(),name="getorder"),
    
    path('token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('signout/', BlacklistTokenUpdateView.as_view(),
         name='signout')
]