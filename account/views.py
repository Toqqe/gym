from django.shortcuts import render
from django.db.models import Count
from django.utils import timezone
from django.db.models.functions import TruncMonth
import time
# Create your views here.
from account.models import UserExercise, Training



def account(request):
    curr_user = request.user

    user_exercises = Training.objects.filter(user=curr_user).order_by('-created')

    user_ex = {}
    for exercise in user_exercises:
        month = exercise.created.strftime("%B")
        if month not in user_ex:
            user_ex[month] = []
        user_ex[month].append(exercise)



    context = {
        "user_exercises" : user_ex,
    }
    
    return render(request, "account/account.html", context)


def training_view(request, id):
    training = Training.objects.get(id=id)

    other_trainings_month = Training.objects.filter(created__month=training.created.month).order_by('created')

    context = {
        "training": training,
        "training_id": id,
        "trainings_month": other_trainings_month
    }
    
    return render(request, "account/training.html", context)