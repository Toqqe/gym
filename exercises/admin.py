from django.contrib import admin

# Register your models here.

from .models import BodyPart, Exercises, UserExercise

class ExercisesModel(admin.ModelAdmin):
    list_display = ['id','name']
    date_hierarchy = 'created'

class UserExerciseModel(admin.ModelAdmin):
    list_display = ['id','user']

admin.site.register(BodyPart, )
admin.site.register(UserExercise, UserExerciseModel)
admin.site.register(Exercises, ExercisesModel)
