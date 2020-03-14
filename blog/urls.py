"""pracdjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path,include
from .views import home,createPost,mypost,updateFormPage,deleteFormPage,allposts,register,profile,deleteAccount,commentAdd
from django.contrib.auth import views as auth_views



urlpatterns = [
    path('',home,name='name_blog_home'),
    path('createPost/',createPost,name='name_blog_createPost'),
    path('mypost/',mypost,name='name_blog_mypost'),
    path('update/<int:pk>',updateFormPage,name='name_blog_update'),
    path('delete/<int:pk>',deleteFormPage,name='name_blog_delete'),
    path('allposts/',allposts,name='name_blog_allposts'),

    path('register/',register,name='name_blog_register'),

    path('login/',auth_views.LoginView.as_view(template_name="blog/login.html"),name='name_login'),
    path('logout/',auth_views.LogoutView.as_view(template_name="blog/logout.html"),name='name_logout'),

    path('profile/',profile,name='name_blog_profile'),
    path('deleteAccount/',deleteAccount,name='name_deleteAccount'),

    path('commentAdd/<int:pk>',commentAdd,name='name_blog_commentAdd'),
    
]

