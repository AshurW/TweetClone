from django.db import models

# Create your models here.
class Tweet(models.Model):
    # id - models.AutoFielfs(primary_key=true)
    content = models.TextField(blank=True, null=True)
    image = models.FileField(upload_to='images/', blank=True, null=True)