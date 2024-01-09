from django.urls import path
from .import views

urlpatterns = [
    path('',views.todos, name='todos'),
    path('update/<int:id>/', views.update_todo, name='update'),
    path('delete/<int:id>/', views.delete_todo, name='delete'),
    path('iscompleted/<int:id>/', views.is_completed, name='iscompleted')
]