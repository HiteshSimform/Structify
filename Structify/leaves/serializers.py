from rest_framework import serializers
from .models import LeaveType, LeaveApplication, LeaveBalance
from employees.serializers import PublicEmployeeSerializer
from users.serializers import CustomUserSerializer


class LeaveTypeSerializer(serializers.ModelSerializer):
    created_by = CustomUserSerializer(read_only=True)
    modified_by = CustomUserSerializer(read_only=True)
    deleted_by = CustomUserSerializer(read_only=True)

    class Meta:
        model = LeaveType
        fields = [
            "id",
            "name",
            "description",
            "max_days",
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


class PublicLeaveTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = LeaveType
        fields = ["id", "name", "max_days"]


class LeaveApplicationSerializer(serializers.ModelSerializer):
    employee = PublicEmployeeSerializer(read_only=True)
    leave_type = PublicLeaveTypeSerializer(read_only=True)
    approver = PublicEmployeeSerializer(read_only=True)
    created_by = CustomUserSerializer(read_only=True)
    modified_by = CustomUserSerializer(read_only=True)
    deleted_by = CustomUserSerializer(read_only=True)

    class Meta:
        model = LeaveApplication
        fields = [
            "id",
            "employee",
            "leave_type",
            "start_date",
            "end_date",
            "reason",
            "status",
            "approver",
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
            "status",
            "approver",
            "created_by",
            "modified_by",
            "deleted_by",
            "deleted_at",
        ]


class LeaveApplicationCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = LeaveApplication
        fields = [
            "id",
            "employee",
            "leave_type",
            "start_date",
            "end_date",
            "reason",
        ]


class LeaveApplicationUpdateStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = LeaveApplication
        fields = ["status", "approver"]


class LeaveBalanceSerializer(serializers.ModelSerializer):
    employee = PublicEmployeeSerializer(read_only=True)
    leave_type = PublicLeaveTypeSerializer(read_only=True)
    created_by = CustomUserSerializer(read_only=True)
    modified_by = CustomUserSerializer(read_only=True)
    deleted_by = CustomUserSerializer(read_only=True)

    class Meta:
        model = LeaveBalance
        fields = [
            "id",
            "employee",
            "leave_type",
            "balance_days",
            "year",
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


class LeaveBalanceCreateUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = LeaveBalance
        fields = [
            "employee",
            "leave_type",
            "balance_days",
            "year",
        ]
