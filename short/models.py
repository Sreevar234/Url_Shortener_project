from django.db import models

# Create your models here.
class short_url(models.Model):
    short_code=models.TextField()
    long_url=models.URLField()
    created_at=models.CharField(max_length=10)
    updated_at=models.CharField(max_length=10)
