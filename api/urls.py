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
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

app_name = "api"

urlpatterns = [
    path('api-auth/', include('rest_framework.urls')),
    path('',ProductList.as_view(),name="productslist"),
    path('product/<str:pk>/',ProductDetail.as_view(),name="productsdetail"),
    path('cart/',CartList.as_view(),name="cartlist"),
    # path('cart/create/', CartCreate.as_view(),name="cartcreate"),
    path('cart/<str:pk>/',CartDetail.as_view(),name="cartdetail"),
    path('user/address/', AddressList.as_view(),name="addresslist"),
    path('placeorder/',OrderList.as_view(),name="placeorder"),

    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('signout/', BlacklistTokenUpdateView.as_view(),
         name='signout')
]