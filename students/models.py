from django.db import models

# Create your models here.

class Students(models.Model):
    id = models.BigAutoField(primary_key=True)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    date_of_birth = models.DateField()
    grade = models.IntegerField()
    phone = models.CharField(max_length=20)
    email = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
