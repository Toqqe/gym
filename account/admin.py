from django.contrib import admin

# Register your models here.
from account.models import UserExercise, Training


class UserExerciseModel(admin.ModelAdmin):
    list_display = ['id','user']


admin.site.register(UserExercise, UserExerciseModel)
admin.site.register(Training)