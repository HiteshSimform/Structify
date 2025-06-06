from rest_framework import serializers
from .models import Department, Employees
from users.serializers import CustomUserSerializer
from designations.serializers import PublicDesignationSerializer


class DepartmentSerializer(serializers.ModelSerializer):
    created_by = CustomUserSerializer(read_only=True)
    modified_by = CustomUserSerializer(read_only=True)
    deleted_by = CustomUserSerializer(read_only=True)

    class Meta:
        model = Department
        fields = [
            "id",
            "name",
            "description",
            "created_by",
            "modified_by",
            "created_at",
            "updated_at",
            "is_deleted",
            "deleted_by",
            "deleted_at",
        ]

        read_only_fields = [
            "created_at",
            "updated_at",
            "created_by",
            "modified_by",
            "deleted_by",
            "deleted_at",
        ]


class PublicDepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = ["id", "name"]


class EmployeeSerializer(serializers.ModelSerializer):
    user = CustomUserSerializer(read_only=True)
    designation = PublicDesignationSerializer(read_only=True)
    department = PublicDepartmentSerializer(read_only=True)

    class Meta:
        model = Employees
        fields = [
            "id",
            "user",
            "phone_number",
            "hire_date",
            "department",
            "designation",
        ]


class PublicEmployeeSerializer(serializers.ModelSerializer):
    department = PublicDepartmentSerializer(read_only=True)
    designation = PublicDesignationSerializer(read_only=True)

    class Meta:
        model = Employees
        fields = [
            "id",
            "user",
            "department",
            "designation",
        ]

    user = CustomUserSerializer(read_only=True)
