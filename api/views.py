from django.http import Http404

from rest_framework import generics
from rest_framework import serializers
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.exceptions import ValidationError

from rest_framework.throttling import UserRateThrottle

from base.models import Product,Cart
from .serializers import ProductSerializer,CartSerializer,CartCreateSerializer

class CustomUserRateThrottle(UserRateThrottle):
    rate= '1/second'

class ProductList(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class CartList(APIView):
    #throttle_classes = [CustomUserRateThrottle]
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        carts = Cart.objects.filter(user=self.request.user)
        serializer = CartSerializer(carts, many=True)
        cart_data=[]
        print(serializer.data)

        for item in serializer.data:

            product = Product.objects.get(pk=item['product'])
            cart_data.append(self.pack_data(product,item['quantity']))
            
        return Response(cart_data)

    def post(self, request, format=None):
        serializer = CartSerializer(data=request.data,context={'request': self.request})

        if serializer.is_valid():
            #print(serializer.data)
            serializer.save()
            product = Product.objects.get(pk=serializer.data['product'])
            item_data = self.pack_data(product,serializer.data['quantity'])

            return Response(item_data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def pack_data(self,item,quantity):

        return {
                'id' : item.pk,
                'name' : item.name,
                'quantity':quantity,
                'unit_price' : item.unit_price,
            }

class CartDetail(APIView):
    permission_classes = [IsAuthenticated]
    def get_object(self, pk):
        try:
            print(type(pk))
            return Cart.objects.get(product_id=pk)
        except Cart.DoesNotExist:
            raise Http404

    def patch(self, request, pk):
        cart_item = self.get_object(int(pk))
        #print(request.data['quantity'])
        serializer = CartSerializer(cart_item, data=request.data, partial=True)
        #serializer = TestModelSerializer(testmodel_object, data=request.data, partial=True) # set partial=True to update a data partially
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data,status=status.HTTP_206_PARTIAL_CONTENT)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        #print("pk type in delete",type(pk))
        cart_item = self.get_object(pk)
        cart_item.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# class CartCreate(generics.CreateAPIView):
#     queryset = Cart.objects.all()
#     serializer_class = CartCreateSerializer

# class CartList(generics.ListCreateAPIView):
#     def get_queryset(self, *args, **kwargs):
#         if self.request.user.is_authenticated:
#             qs = Cart.objects.all()
#             qs = qs.filter(user=self.request.user)
#             return qs
#         else:
#             raise ValidationError({"error": ["You don't have enough permission."]})
#     # queryset = get_queryset()
#     serializer_class = CartSerializer(depth=1)
# class CartDetail(generics.RetrieveUpdateDestroyAPIView):
#     def get_queryset(self, *args, **kwargs):
#         if self.request.user.is_authenticated:
#             qs = Cart.objects.all()
#             qs = qs.filter(user=self.request.user)
#             return qs
#         else:
#             raise ValidationError({"error": ["You don't have enough permission."]})
#     serializer_class = CartCreateSerializer

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