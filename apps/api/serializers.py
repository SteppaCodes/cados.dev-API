from rest_framework import serializers

from . models import Advocate, Company

class CompanySerializer(serializers.ModelSerializer):
    employee_count = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Company
        fields = [
            "id",
            "name",
            "bio",
            "employee_count",
        ]

    def get_employee_count(self, obj):
        count= obj.employees.count()
        return count

class AdvocateSerializer(serializers.ModelSerializer):
    company = CompanySerializer()
    class Meta:
        model = Advocate
        fields = [
            "id",
            "name", 
            "bio",
            "company"
        ]