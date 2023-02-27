from django.conf.urls import path
from Student_Admin_APP import views


url_patterns = [
    path(r'^student_administration$', views.student_administration_Api),
    path(r'^student_administration/([0-9]+)$', views.student_administration_Api)
]
