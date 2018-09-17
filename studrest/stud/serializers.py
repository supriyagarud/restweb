from rest_framework import serializers
from . import models


class StudentSerializer(serializers.ModelSerializer):

    class Meta:
        fields = ('id', 'name', 'age', 'gender','skill','country','remark','created_at', 'updated_at','is_active')
        model = models.Student