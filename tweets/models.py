from django.db import models
from django.conf import settings

User = settings.AUTH_USER_MODEL

import random

# Create your models here.
class Tweet(models.Model):
    # id - models.AutoFielfs(primary_key=true)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField(blank=True, null=True)
    image = models.FileField(upload_to='images/', blank=True, null=True)

    # def __str__(self):
    #     return self.content

    class Meta:
        ordering = ['-id']

    def serialize(self):
        return {
            "id": self.id,
            "content": self.content,
            "likes": random.randint(0, 100)
        }