from base.models import Product,Cart
from .serializers import ProductSerializer,CartSerializer,CartCreateSerializer
from rest_framework import generics
from rest_framework import serializers

from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.exceptions import ValidationError


class ProductList(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class CartCreate(generics.CreateAPIView):
    queryset = Cart.objects.all()
    serializer_class = CartCreateSerializer

class CartList(generics.ListCreateAPIView):
    def get_queryset(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            qs = Cart.objects.all()
            qs = qs.filter(user=self.request.user)
            return qs
        else:
            raise ValidationError({"error": ["You don't have enough permission."]})
    # queryset = get_queryset()
    serializer_class = CartSerializer
class CartDetail(generics.RetrieveUpdateDestroyAPIView):
    def get_queryset(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            qs = Cart.objects.all()
            qs = qs.filter(user=self.request.user)
            return qs
        else:
            raise ValidationError({"error": ["You don't have enough permission."]})
    serializer_class = CartCreateSerializer

class BlacklistTokenUpdateView(APIView):
    permission_classes = [AllowAny]
    authentication_classes = ()

    def post(self, request):
        try:
            refresh_token = request.data["refresh_token"]
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response(status=status.HTTP_205_RESET_CONTENT)
        except Exception as e:
            return Response(status=status.HTTP_400_BAD_REQUEST)