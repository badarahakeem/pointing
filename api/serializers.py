# import serializer from rest_framework
from rest_framework import serializers
from eqrApp.models import Employee, Pointing




# create a serializer

class PointingSerlializer(serializers.ModelSerializer):
    class Meta:
        model = Pointing
        fields = "__all__"

class EmployeeSerlializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = "__all__"



class CheckEmpForm(serializers.Serializer):
	# initialize fields
	id = serializers.IntegerField(read_only=True)
