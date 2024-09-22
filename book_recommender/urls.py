"""
URL configuration for book_recommender project.

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

from django.contrib.auth.models import User
from django.urls import include, path
from rest_framework import routers
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
router = routers.DefaultRouter()
from django.contrib import admin
from django.urls import path, include
from book_recommender import views


# Routers provide a way of automatically determining the URL conf.
router = routers.DefaultRouter()

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('', include('rest_framework.urls', namespace='rest_framework')),
    path('admin/', admin.site.urls),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),   
    path('register/', views.RegisterView.as_view(), name='auth_register'),
    path('accounts/profile/', views.getProfile, name='profile'),
    path('accounts/profile/update/', views.updateProfile, name='update-profile'),
    path('books/', views.BookViewSet.as_view({'get': 'list'})),  
    path('books/<int:pk>/', views.BookDetail.as_view()),
    path('authors/', views.AuthorViewSet.as_view({'get': 'list'})),  
    path('authors/<int:pk>/', views.AuthorDetail.as_view()),
    path('books_shelf/', views.BookShelfViewSet.as_view({'get': 'list'})),
    path('favorite_book/', views.FavoriteBooksViewSet.as_view({'get': 'list'})),
    path('suggested_books/', views.SuggestedBooks.as_view())
]