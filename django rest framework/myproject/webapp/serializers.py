from rest_framework import serializers
from .models import Employee


class EmployeeSerializers(serializers.ModelSerializer):
    class Meta:  # for configuration
        model = Employee
        fields = '__all__'  # it will return all the fields in a model

#       fields = ('first_name', 'last_name')  # particular model

