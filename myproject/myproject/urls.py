"""
URL configuration for myproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from myapp import views

# urlpatterns = [
#     path('admin/', admin.site.urls),

#     path("welcome/",views.home),
#     path('one/',views.show, name='show'), 
#     path('about/',views.about,name='about'),
#      path('color/',views.color,name='color'),
#     path('bootstrab/',views.bootstrab,name='bootstrab'),

#     path('home/', views.home, name='home'),
#     path('page1/', views.page1, name='page1'),
#     path('page2/', views.page2, name='page2'),
#     path('page3/', views.page3, name='page3'),

#     path('form/',views.submit_form,name='submit_form'),
#     path('email/',views.contact_view, name='contact'),
#     path('create-product/',views.create_product, name='create_product'),
#     path('products/',views.product_list, name='product_list'),


#     # path('create-course/',views.create_course, name='create_course'),
#     path('courses/', views.course_list, name='course_list'),
#     path('enroll-student/',views.enroll_student, name='enroll_student'),


#      path('create/', views.item_create, name='item_create'),
#      path('read/', views.item_list, name='item_list'),
#      path('<int:pk>/', views.item_detail, name='item_detail'),
#      path('<int:pk>/edit/', views.item_update, name='item_update'),

#      path('<int:pk>/delete/', views.item_delete, name='item_delete'),


#     path('register/', views.user_register, name='register'),
#     path('login/', views.user_login, name='login'),
#     path('logout/', views.user_logout, name='logout'),
# ]


# from django.urls import path, include
# from rest_framework.routers import DefaultRouter
# from drfapp import views


# from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

# router = DefaultRouter()
# router.register(r'products', views.ProductViewSet,basename='product')

# urlpatterns = [
#     path('', include(router.urls)),
#     path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
#     path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
# ]





# urlpatterns = [
#     path('products/', views.ProductAPIView.as_view(), name='product-list-create'),  # GET & POST
#     path('products/<int:pk>/',views.ProductAPIView.as_view(), name='product-detail'),  # GET, PUT, PATCH, DELETE
# ]



from django.contrib import admin
from django.urls import path
from drfapp import views

urlpatterns = [
   
    path('admin/', admin.site.urls),
    path('protected/', views.main_view, name='protected_view'),
    path('login/', views.login_view, name='login'),
    path('public/', views.public_view, name='public'),
]