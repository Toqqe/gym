from django.contrib import admin

# Register your models here.

from .models import BodyPart, Exercises
from account.models import UserExercise

class ExercisesModel(admin.ModelAdmin):
    list_display = ['id','name']
    date_hierarchy = 'created'


admin.site.register(BodyPart, )

admin.site.register(Exercises, ExercisesModel)
