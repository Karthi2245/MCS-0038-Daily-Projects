from rest_framework import serializers
from rest_framework import Employee


class EmployeeSerializers(serializers.ModelSerializer):
    class Meta:  # for configuration
        model = Employee
        fields = '_all__'  # it will return all the fields in a model

#       fields = ('first_name', 'last_name')  # particular model



