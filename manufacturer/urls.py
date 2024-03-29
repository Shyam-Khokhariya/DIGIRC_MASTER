"""DigiRC URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path, include
from . import views
from users import views as users_views

urlpatterns = [
    path('dashboard/', views.Dashboard.as_view(), name='manufacturer-dashboard'),
    # path('dashboard/', views.chart, name='manufacturer-dashboard'),
    path('dashboard/add/', views.add_vehicle, name='manu-add-vehicle'),
    path('dashboard/display/manufactured/', views.DisplayManufactured.as_view(), name='manu-display-manufactured'),
    path('dashboard/vehicle/<str:pk>', views.DisplayVehicleDetail.as_view(),
         name='manu-display-vehicle-detail'),
    path('register/', users_views.register, name='manu-signup'),
]
