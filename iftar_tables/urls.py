from django.urls import path
from . import views

urlpatterns = [
   path('',views.home,name='home'),
   path('add_table/',views.add_table,name='add_table'),
]