

from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name='home'),
    path('student/<int:id>/', views.student_detail, name='detail'),
    path('add/', views.add_student, name='add'),
    path('edit/<int:id>/', views.edit_student, name='edit'),
    path('delete/<int:id>/', views.delete_student, name='delete'),
]