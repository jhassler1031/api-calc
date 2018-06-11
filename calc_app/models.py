from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    pass

class Operation(models.Model):
    operand_one = models.IntegerField()
    operand_two = models.IntegerField()
    operator = models.CharField(max_length=1)
    result = models.IntegerField(null=True)
    created = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
