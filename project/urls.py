from django.contrib import admin
from django.urls import path
from pharmacy import views

urlpatterns = [
    path('medicine/', views.medicineView, name='medicine'),
    path('medicineUpdate/<str:pk>', views.medicineUpdateView, name='updateMedicine'),
    path('deleteMedicine/<str:pk>', views.medicineDeleteView, name='deleteMedicine'),

    path('sales/', views.selesView, name='sales'),
    path('salesUpdate/<str:pk>', views.saleUpdateView, name='salesUpdate'),
    path('salesDelete/<str:pk>', views.saleDeleteView, name='salesDelete'),

    path('customer/', views.customerView, name='customer'),
    path('customerUpdate/<str:pk>', views.customerUpdateView, name='customerUpdate'),
    path('customerDelete/<str:pk>', views.customerDeleteView, name='customerDelete'),

    path('lons/', views.lonsView, name='lons'),
    path('lonsUpdate/<str:pk>', views.lonsUpdateView, name='lonsUpdate'),
    path('lonsDelete/<str:pk>', views.lonsDeleteView, name='lonsDelete'),

    path('', views.loginView, name='login'),
    path('home/', views.homeView, name='home'),
]
