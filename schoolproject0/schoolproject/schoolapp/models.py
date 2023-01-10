from django.db import models
from django.db.models.deletion import CASCADE


class department(models.Model):
    departmentname = models.CharField(max_length=100)

    def __str__(self):
        return str(self.departmentname)

class employee(models.Model):
    deptid = models.ForeignKey(department, on_delete=CASCADE)
    empname = models.CharField(max_length=100)

    def __str__(self):
        return str(self.empname)