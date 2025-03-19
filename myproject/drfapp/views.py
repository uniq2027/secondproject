


#__________________________________________________________________________

# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework import status
# from django.shortcuts import get_object_or_404
# from .models import Product
# from .serializers import ProductSerializer

# class ProductAPIView(APIView):
#     """
#     API View to demonstrate handling GET, POST, PUT, PATCH, and DELETE requests manually.
#     """

#     def get(self, request, pk=None):
#         """Handles GET requests: List all products or retrieve a single product."""
#         if pk:
#             product = get_object_or_404(Product, pk=pk)
#             serializer = ProductSerializer(product)
#             return Response(serializer.data, status=status.HTTP_200_OK)
        
#         products = Product.objects.all()
#         serializer = ProductSerializer(products, many=True)
#         return Response(serializer.data, status=status.HTTP_200_OK)

#     def post(self, request):
#         """Handles POST requests: Create a new product."""
#         serializer = ProductSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def put(self, request, pk):
#         """Handles PUT requests: Fully update an existing product."""
#         product = get_object_or_404(Product, pk=pk)
#         serializer = ProductSerializer(product, data=request.data)  # Full update
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_200_OK)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def patch(self, request, pk):
#         """Handles PATCH requests: Partially update an existing product."""
#         product = get_object_or_404(Product, pk=pk)
#         serializer = ProductSerializer(product, data=request.data, partial=True)  # Partial update
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_200_OK)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def delete(self, request, pk):
#         """Handles DELETE requests: Remove a product."""
#         product = get_object_or_404(Product, pk=pk)
#         product.delete()
#         return Response({"message": "Product deleted successfully"}, status=status.HTTP_204_NO_CONTENT)

#_____________________________________________________________

# GENERIC VIEW:

#ListAPIView: Handles listing objects (GET).
#CreateAPIView: Handles creating a new object (POST).
#RetrieveAPIView: Handles retrieving a single object (GET).
#UpdateAPIView: Handles updating an object (PUT/PATCH).
#DestroyAPIView: Handles deleting an object (DELETE).


#ListCreateAPIView: Handles both listing and creating objects (GET, POST).

#RetrieveUpdateDestroyAPIView: Handles retrieving, updating, and deleting an object (GET, PUT, PATCH, DELETE).


# from rest_framework.generics import ListAPIView,CreateAPIView,RetrieveUpdateDestroyAPIView
# from .models import Product
# from .serializers import ProductSerializer

# class ProductAPIView(ListAPIView):
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer
   
# class ProductAPIView(CreateAPIView):
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer
   
# class ProductAPIView(RetrieveUpdateDestroyAPIView):
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer


# _____________________________________________________
# from django.shortcuts import render

# Create your views here.
# from rest_framework import viewsets,filters
# from .models import Product
# from .serializers import ProductSerializer
# from rest_framework.pagination import PageNumberPagination

# class ProductViewSet(viewsets.ModelViewSet):
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer
#     pagination_class =PageNumberPagination
#     filter_backends = [filters.SearchFilter]
#     search_fields = ['name']

from django.shortcuts import redirect
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse

def main_view(request):
    return HttpResponse("This is a protected route. You have access!")



def login_view(request):
     if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)  # Logs the user in
            return redirect('/protected/')  # Redirects to the protected route
        else:
            return HttpResponse("Invalid credentials. Try again.")

     return HttpResponse("Login Page - Send POST request with username and password.")
    

def public_view(request):
    return HttpResponse("This is a public page.")
