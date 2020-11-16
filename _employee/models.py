import random

from django.db import models
from django.urls import reverse

from phonenumber_field.modelfields import PhoneNumberField


# Create your models here.
class employeeDB(models.Model):
    employee_id = models.CharField(max_length=15, null=True, blank=True)
    first_name = models.CharField(max_length=24, null=False, blank=False)
    last_name = models.CharField(max_length=24, null=True, blank=True)
    address = models.TextField(max_length=255, null=False, blank=False)
    phone = PhoneNumberField(blank=False)
    email = models.EmailField(max_length=64)
    image = models.ImageField()

    def __str__(self):
        if self.first_name and self.last_name:
            return self.first_name+' '+self.last_name
        else:
            return self.first_name

    def save(self):
        if not (self.id and self.employee_id):
            self.employee_id = random.randint(100000, 1000000)
        return super(employeeDB, self).save()

    def get_absolute_url(self):
        return reverse('employee:detail', kwargs={'pk': self.pk})