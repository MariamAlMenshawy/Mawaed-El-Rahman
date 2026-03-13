from django.urls import path
from . import views

urlpatterns = [
  path('',views.home,name='home'),
  path('add_table/',views.add_table,name='add_table'),
  path('table/<int:table_id>/',views.table_detail,name='table_detail'),
  path('table/<int:table_id>/update/',views.UpdateTable.as_view(),name='update_table'),
  path('table/<int:table_id>/update/delete/',views.DeleteTable.as_view(),name='delete_table'),

 ]