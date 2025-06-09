from django.shortcuts import render
from rest_framework import generics, permissions, status

# Create your views here.
from .models import LeaveType, LeaveBalance, LeaveApplication
from .serializers import (
    LeaveTypeSerializer,
    PublicLeaveTypeSerializer,
    LeaveApplicationSerializer,
    LeaveApplicationCreateSerializer,
    LeaveApplicationUpdateStatusSerializer,
    LeaveBalanceSerializer,
    LeaveBalanceCreateUpdateSerializer,
)

from users.permissions import IsMainAdminOrReadOnly
from django.utils import timezone
from .permissions import IsManagerHrOrAdmin


class LeaveTypeListCreateAPIView(generics.ListCreateAPIView):
    queryset = LeaveType.objects.filter(is_deleted=False)
    serializer_class = LeaveTypeSerializer
    permission_classes = [permissions.IsAuthenticated, IsManagerHrOrAdmin]

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user, modified_by=self.request.user)


class LeaveTypeRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = LeaveType.objects.filter(is_deleted=False)
    serializer_class = LeaveTypeSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_update(self, serializer):
        serializer.save(modified_by=self.request.user)

    def perform_destroy(self, instance):
        instance.is_deleted = True
        instance.deleted_by = self.request.user
        instance.deleted_at = timezone.now()
        instance.save()


class LeaveApplicationListCreateAPIView(generics.ListCreateAPIView):
    queryset = LeaveApplication.objects.filter(is_deleted=False)
    permission_classes = [permissions.IsAuthenticated]

    def get_serializer_class(self):
        if self.request.method == "POST":
            return LeaveApplicationCreateSerializer
        return LeaveApplicationSerializer

    def perform_create(self, serializer):
        serializer.save(
            created_by=self.request.user,
            modified_by=self.request.user,
        )


class LeaveApplicationRetriveAPIView(generics.RetrieveAPIView):
    queryset = LeaveApplication.objects.filter(is_deleted=False)
    serializer_class = LeaveApplicationSerializer
    permission_classes = [permissions.IsAuthenticated]


class LeaveApplicationStatusUpdateAPIView(generics.UpdateAPIView):
    queryset = LeaveApplication.objects.filter(is_deleted=False)
    serializer_class = LeaveApplicationUpdateStatusSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_update(self, serializer):
        serializer.save(modified_by=self.request.user)


class LeaveBalanceListCreateAPIView(generics.ListCreateAPIView):
    queryset = LeaveBalance.objects.filter(is_deleted=False)
    permission_classes = [permissions.IsAuthenticated]

    def get_serializer_class(self):
        if self.request.method == "POST":
            return LeaveBalanceCreateUpdateSerializer
        return LeaveBalanceSerializer

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user, modified_by=self.request.user)


class LeaveBalanceRetriveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = LeaveBalance.objects.filter(is_deleted=False)
    permission_classes = [permissions.IsAuthenticated]

    def get_serializer_class(self):
        if self.request.method == "GET":
            return LeaveBalanceSerializer
        return LeaveBalanceCreateUpdateSerializer

    def perform_update(self, serializer):
        serializer.save(modified_by=self.request.user)

    def perform_destroy(self, instance):
        instance.is_deleted = True
        instance.deleted_by = self.request.user
        instance.deleted_at = timezone.now()
        instance.save()
