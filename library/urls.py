"""library URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('book/', views.book, name='book'),
    path('book/add_book/<int:id>/', views.add_book, name='add_book'),
    path('delete_item/<int:id>/', views.delete_item, name='delete_item'),
    path('student/', views.student, name='student'),
    path('staff/', views.staff, name='staff'),
    path('borrow/', views.borrow, name='borrow'),
    path('return1/',views.return1, name='return1'),
    path('lost/', views.lost, name='lost')
]
