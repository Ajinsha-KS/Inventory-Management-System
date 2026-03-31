from django.urls import path
from . import views

urlpatterns = [
    path('',views.dashboard, name='dashboard'),
    path('add/',views.add_product,name='add_product'),
    path('edit/<int:id>/',views.edit_product,name='edit_product'),
    path('delete/<int:id>/',views.delete_product,name='delete_product'),
    path('transaction/',views.add_transaction,name='transaction'),
    path('transactionhistory/',views.transaction_history,name='transaction_history'),
]