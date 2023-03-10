from django.urls import re_path
from Student_Admin_APP import views


urlpatterns = [
    re_path(r'^std_admin$', views.student_administration_Api),
    re_path(r'^std_admin/([0-9]+)$', views.student_administration_Api),
]
