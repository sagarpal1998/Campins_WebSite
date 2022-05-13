"""Project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from unicodedata import name
from django import views
from django.contrib import admin
from django.urls import path
from testapp.views import Page4, Page6
from testapp.views import Page3
from testapp import views

urlpatterns = [
    path('',views.Home,name='home'),
    path('show',views.show,name='welldone'),
    path('<int:id>', views.update,name='update_url'),
    path('delet/<int:id>',views.remove,name='remove_url'),
    path('card/<int:id>',views.card,name="card_url"),
    path('Page2',views.Page2,name='page2'),
    path('Page3',views.Page3,name= 'page3'),
    path('Page4',views.Page4,name='page4'),
    path('Page5',views.Page5,name='page5'),
    path('Page6',views.Page6,name='page6'),
    path('register',views.register,name='register'),
    path('login',views.login,name='login'),
    path('logout',views.logout,name='logout'),
    

]
