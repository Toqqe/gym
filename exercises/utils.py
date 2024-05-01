from .models import BodyPart, UserExercise, Exercises
from django.contrib.auth.models import User
from django.utils import timezone

def createParts():
    list_exc = ['shoulders', 'biceps', 'chest', 'abs', 'abs_obliques', 'quads', 'knees', 'shins', 'wrists', 'forearms', 'hips', 'adductors', 'neck', 'foots']

    for i in list_exc:
        model = BodyPart.objects.create(name=i)

def CreateRandomEx():
    test_us = User.objects.get(id=1)
    test_ex = Exercises.objects.all()
    
    id_test_ex = [ ex_id.id for ex_id in test_ex]
    for i in range(5):
        
        test_ex_instance = Exercises.objects.get(id=id_test_ex[0])
        test = UserExercise(user=test_us, exercise=test_ex_instance, reps=1, sets=1, kg=1, created=timezone.now() - timezone.timedelta(days=7))
        #UserExercise.objects.create(user=test_us, exercise=test_ex_instance, reps=1, sets=1, kg=1, created=timezone.now() - timezone.timedelta(days=i))
        test.save()