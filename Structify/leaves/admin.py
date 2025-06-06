from django.contrib import admin
from .models import LeaveApplication, LeaveBalance, LeaveType

# Register your models here.
admin.site.register(LeaveApplication)
admin.site.register(LeaveBalance)
admin.site.register(LeaveType)
