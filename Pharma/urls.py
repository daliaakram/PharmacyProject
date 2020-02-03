from django.contrib import admin
from django.urls import path,include
from Pharma import views

app_name = 'Pharma'

urlpatterns = [
    path('', views.home_page, name='home'),
    path('medicine/', views.list_medicine, name='medicine'),
    path('transactions/', views.list_transactions, name='transactions'),
]
