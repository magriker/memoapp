"""
URL configuration for memoapp project.

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
from memo import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.TopView.as_view(), name="top"),
    path("memo/new", views.MemoCreateView.as_view(), name="form"),
    path("memo/", views.MemoListView.as_view(), name="list"),
    path("memo/edit/<int:pk>", views.MemoUpdateView.as_view(), name="edit"),
    path("crud/delete/<int:pk>", views.MemoDeleteView.as_view(), name="delete"),
]
