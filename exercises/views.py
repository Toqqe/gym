import json
from datetime import timedelta

from django.utils import timezone
from django.db.models import Count
from django.shortcuts import render
from django.views import View
from django.http import JsonResponse
# Create your views here.

from exercises.models import BodyPart, Exercises, UserExercise

def index(request):
    curr_user = request.user
    ## Add user etc.
    today = timezone.now().date()
    exercise_dates = UserExercise.objects.values('created__date').annotate(count_ex=Count('id')).order_by('created__date') 

    user_ex = {}
    for entry in exercise_dates:
        date = entry['created__date'] # 2024-04-29
        #print(timezone.now().date()) # 2024-04-30
        if date != today:
            user_ex[date] = [] ## Empty list for today
        exercises = UserExercise.objects.filter(created__date=date)
        exercise_list = [ex for ex in exercises]
        user_ex[date] = exercise_list

        
    context = {
        "user_ex_dict" : user_ex
    }
    
    return render(request, "exercises/index.html", context)

def choosed_part_modal(request, part):
    modal_template = "exercises/modal/part_modal_items.html"
    body_part = BodyPart.objects.filter(name=part).first()
    
    exercises = Exercises.objects.filter(part=body_part).order_by("-id")[:5]
    
    context = {
        "body_part": str(body_part),
        "exercises":exercises
    }
    
    return render(request, modal_template, context)

def add_exercise(request):
    ## b'{"inputExercise":"d","bodyPart":"abs_obliques","inputReps":"1"}'
    
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            ## DATA
            inputExercise = data.get('inputExercise')
            bodyPart = data.get('bodyPart')
            inputReps = data.get('inputReps')
            inputSets = data.get('inputSets')
            inputKG = data.get('inputKG')

        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON'}, status=400)
        
        user = request.user
        part = BodyPart.objects.filter(name=bodyPart).first()
        check_exercise = Exercises.objects.filter(name__iexact=inputExercise, part__name=bodyPart).first()
        print(check_exercise)
        if check_exercise:
            new_user_exercise = UserExercise(user=request.user, exercise=check_exercise ,sets=inputSets, reps=inputReps, kg=inputKG)
            new_user_exercise.save()
            return JsonResponse({'success': True, 'message': 'Exercise added to user!'})

        
        new_exercise = Exercises(name=inputExercise, user=user ,part=part) #, sets=inputSets, reps=inputReps)
        new_exercise.save()
        
        new_user_exercise = UserExercise(user=request.user, exercise=new_exercise, sets=inputSets, reps=inputReps, kg=inputKG)
        new_user_exercise.save()
        
        return JsonResponse({
            'success':True,
            'message':'Exercise created and added to user!'
        })
        
def search_exercises(request, query):
    body_part = BodyPart.objects.filter(name=query).first()
    created_ex = Exercises.objects.filter(part=body_part)

    return JsonResponse({
        'success':True,
        'exercises': [ ex_for_parts.name for ex_for_parts in created_ex ]
    })


def exercises(request):
    return 