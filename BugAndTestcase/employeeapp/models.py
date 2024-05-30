from django.db import models
from adminsapp.models import *
# Create your models here.

class Testcase(models.Model):
    project_name=models.CharField(max_length=350)
    module_name=models.CharField(max_length=350)
    senario=models.CharField(max_length=350)
    description=models.CharField(max_length=350)
    input_data=models.CharField(max_length=350)
    type_of_exception=models.CharField(max_length=350)
    pre_condition=models.CharField(max_length=350)
    expected_actual_result=models.CharField(max_length=350)
    status=models.CharField(max_length=300)
    date_of_creation=models.DateField()
    tester_email=models.EmailField()

class Bug(models.Model):
    testcase_id=models.IntegerField()
    description=models.CharField(max_length=350)
    test_path=models.CharField(max_length=300)
    screenshot=models.ImageField(upload_to="images/")
    sevearity=models.CharField(max_length=300)
    priority=models.CharField(max_length=300)
    status=models.CharField(max_length=300)
    date=models.DateField()
    tested_by_email=models.EmailField()

