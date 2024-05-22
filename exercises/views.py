import json
from datetime import timedelta

from django.utils import timezone
from django.db.models import Count
from django.shortcuts import render
from django.views import View
from django.http import JsonResponse
# Create your views here.

from exercises.models import BodyPart, Exercises
from account.models import UserExercise, Training

def index(request):
    
    ## For anonymouseusers
    # request.session.save()
    # session_key = request.session.session_key || to add
    
    curr_user = request.user
    today = timezone.now().date()
    
    exercise_dates = UserExercise.objects.filter(user=curr_user).values('created__date').annotate(count_ex=Count('id')).order_by('created__date') 

    user_ex = {}
    for entry in exercise_dates:
        date = entry['created__date'] # 2024-04-29
        
        exercises = UserExercise.objects.filter(created__date=date)
        exercise_list = [ex for ex in exercises]
        user_ex[date] = exercise_list
        
    if today not in user_ex.keys():
        user_ex[today] = []
        
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
    
    if request.method == 'POST' and request.user.is_authenticated:
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
        today = timezone.now()
        part = BodyPart.objects.filter(name=bodyPart).first()
        
        new_exercise = Exercises.objects.filter(name__iexact=inputExercise, part__name=bodyPart).first()
        today_training = Training.objects.filter(user=user, created__date=today.date()).first()
        
        if today_training is None:
            today_training = Training.objects.create(user=user, created=today)
        
        if not new_exercise:
            new_exercise = Exercises(name=inputExercise, user=user ,part=part) 
            new_exercise.save()


        new_user_exercise = UserExercise(user=request.user, exercise=new_exercise, sets=inputSets, reps=inputReps, kg=inputKG)
        new_user_exercise.save()
        today_training.exercises.add(new_user_exercise)
        
        return JsonResponse({
            'success':True,
            'message':'Exercise created and added to user!',
            'exercise_id':new_user_exercise.id
        })
        
def get_exercise(request, id):
    modal_template = "exercises/modal/edit_modal_item.html"
    exercise = UserExercise.objects.get(id=id)

    context = {
        "exercise": exercise,
    }
    
    return render(request, modal_template, context)
    
def edit_exercise(request):
    
    if request.method == "POST" and request.user.is_authenticated:
        try:
            data = json.loads(request.body)
            idExercise = data.get('idExercise')
            inputReps = data.get('inputReps')
            inputSets = data.get('inputSets')
            inputKG = data.get('inputKG')
        except json.JSONDecodeError:
            return JsonResponse({'error":"Invalid JSON'}, status=400)
        
        exercise = UserExercise.objects.get(id = idExercise)
        
        if exercise.user == request.user:
            exercise.reps = inputReps
            exercise.sets = inputSets
            exercise.kg = inputKG
            exercise.save()
        else:
            return JsonResponse({'error":"Invalid user'}, status=400)
        
        return JsonResponse({
            'success':True,
            'message': "Exercise updated!"
            })
        
def delete_exercise(request):
    if request.method == "POST" and request.user.is_authenticated:
        try:
            data = json.loads(request.body)
            idExercise = data.get('idExercise')
        except json.JSONDecodeError:
            return JsonResponse({'error":"Invalid JSON'}, status=400)
        
        exercise = UserExercise.objects.get(id = idExercise)
        
        if exercise.user == request.user:
            exercise.delete()
        else:
            return JsonResponse({'error":"Invalid user'}, status=400)
        
        return JsonResponse({
            'success':True,
            'message': "Exercise deleted!"
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