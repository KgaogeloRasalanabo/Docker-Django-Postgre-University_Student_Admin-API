from rest_framework import serializers
from Student_Admin_APP.models import Student_administration


class Student_administration_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Student_administration
        field = ('name','surname','id_no','course_id','course_name','Course_code')
