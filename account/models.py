from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

from exercises.models import Exercises
# Create your models here.


class UserExercise(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    exercise = models.ForeignKey(Exercises, on_delete=models.CASCADE, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=False)
    sets = models.IntegerField(default=0)
    reps = models.IntegerField(default=0)
    kg = models.IntegerField(default=0)
    
    def save(self, *args, **kwargs):
        if not self.created:
            self.created = timezone.now()
        super().save(*args, **kwargs)    

    def __str__(self):
        return str(self.user)
    
class Training(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=False)
    exercises = models.ManyToManyField(UserExercise)
