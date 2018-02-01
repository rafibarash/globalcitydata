"""globalcitydata URL Configuration

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
from django.urls import path
from . import views

app_name = 'data'

urlpatterns = [
    # Dataset Detail view
    path('<str:slug>/', views.dataset_detail, name='dataset_detail'),
    # Must be last
    # Home/List view, with filter
    path('', views.dataset_list, name='dataset_list'),
    # path('', views.MainListView.as_view(), name='dataset_list')
]