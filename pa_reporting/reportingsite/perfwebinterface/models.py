from django.db import models
from django.contrib.auth.models import User

class c100_mp_3_8x10G(models.Model):
    test_name = models.CharField(max_length=100)
    build = models.CharField(max_length=30)
    test_type = models.CharField(max_length=20)
    results = models.IntegerField()
    id = models.ForeignKey(User, on_delete=models.CASCADE, primary_key=True)

