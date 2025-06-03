from django.db import models

# Create your models here.
class Employee(models.Model):
    employee_id = models.IntegerField()
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(_(""), max_length=254)
    phone_number =  models.CharField(max_length=10)
    hire_date = models.DateTimeField()
    