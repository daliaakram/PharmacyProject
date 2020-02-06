from django.contrib import admin
from django.urls import path,include
from Pharma import views

app_name = 'Pharma'

urlpatterns = [
    # path('', views.home_page, name='home'),
    path('createmed/', views.create_med, name='createmed'),
    path('createtrans/', views.create_trans, name='createtrans'),
    path('medicine/', views.list_medicine, name='medicine'),
    path('transactions/', views.list_transactions, name='transactions'),
    path('', views.get_loggedin_user, name='getname'),
    path('update/<int:id>', views.update_medicine, name="update"),
    path('delete/<int:id>', views.delete_medicine, name="delete"),
    path('updatetrans/<int:id>', views.update_transaction, name="tupdate"),
    path('deletetrans/<int:id>', views.delete_transaction, name="tdelete"),
]
