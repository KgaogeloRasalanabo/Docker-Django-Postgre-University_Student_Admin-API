from django.urls import re_path
from Student_Admin_APP import views


urlpatterns = [
    re_path(r'^student_administration$', views.student_administration_Api),
    re_path(r'^student_administration/([0-9]+)$', views.student_administration_Api),
]
