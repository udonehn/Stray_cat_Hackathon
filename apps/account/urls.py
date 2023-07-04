"""cat_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import path
from . import views


urlpatterns = [
    path('', views.main, name = 'main'),
    path('login/', views.login, name = 'login'),
    path('logout/', views.logout, name = 'logout'),
    path('signup/', views.signup, name = 'signup'),
    path('mypage/', views.mypage, name = 'mypage'),
    path('bookmark/', views.bookmark, name = 'bookmark'),
    path('detail/<str:cat_id>/', views.detail, name = 'detail'),
    path('mypage/', views.mypage, name = 'mypage'),
    path('url_test/', views.url_test, name = 'url_test'),

    #Api
    path('cat_food_Api/<str:cat_id>/', views.cat_food_Api, name='cat_food_Api'),
    path('cat_snack_Api/<str:cat_id>/', views.cat_snack_Api, name='cat_snack_Api'),
]
