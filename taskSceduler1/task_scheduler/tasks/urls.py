# tasks/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('admin/', views.admin_task_list, name='admin_task_list'),
    path('add/', views.add_task, name='add_task'),
    path('edit/<int:task_id>/', views.edit_task, name='edit_task'),
    path('delete/<int:task_id>/', views.delete_task, name='delete_task'),
    path('delete_all/', views.delete_all_tasks, name='delete_all_tasks'),
    path('worker/', views.worker_task_list, name='worker_task_list'),
    path('tester/', views.tester_task_list, name='tester_task_list'),
    path('task/complete/<int:task_id>/', views.mark_task_completed, name='mark_task_completed'),
    path('assign_task/', views.assign_task, name='assign_task'),
]

