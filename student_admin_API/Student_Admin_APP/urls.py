from django.urls import path
from Student_Admin_APP import views


urlpatterns = [
    path('student_administration', views.student_administration_Api),
    path('student_administration/([0-9]+)/', views.student_administration_Api),
]
