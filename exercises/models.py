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
    # sets = models.IntegerField(default=0)
    # reps = models.IntegerField(default=0)
    #kg = models.IntegerField(default=0)

    def __str__(self):
        return self.name

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
#     sets = models.IntegerField(default=0)
#     reps = models.IntegerField(default=0)

