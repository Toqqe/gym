from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.

class BodyPart(models.Model):
    name = models.CharField(max_length=100)

    def save(self, *args,**kwargs):
        existing_body_part = BodyPart.objects.filter(name=self.name).first()
        if existing_body_part:
            return 
        super(BodyPart, self).save(*args, **kwargs)

    def __str__(self):
        return self.name

class Exercises(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    name = models.CharField(max_length=100)
    part = models.ForeignKey(BodyPart, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name

