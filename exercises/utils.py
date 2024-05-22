from .models import BodyPart, Exercises
from account.models import UserExercise
from django.contrib.auth.models import User
from django.utils import timezone

def createParts():
    list_exc = ['shoulders', 'biceps', 'chest', 'abs', 'abs_obliques', 'quads', 'knees', 'shins', 'wrists', 'forearms', 'hips', 'adductors', 'neck', 'foots', 'trapezius', 'lats', 'triceps', 'glutes', 'hamstrings', 'calfs', 'ankles', 'rear_deltoids', 'lower_back', 'elbows', 'hand_fingers']

    for i in list_exc:
        model = BodyPart.objects.create(name=i)

def createExercisesLorem():
    test_us = User.objects.get(id=1)
    exercises = ["Nulla ut metus et ligula malesuada feugiat.", "Donec a orci mattis diam pellentesque euismod a vitae tellus.", "Quisque fringilla diam ut nisi maximus, in fringilla tortor vulputate.", "Etiam sed velit eget arcu hendrerit pellentesque vitae non nunc.", "Integer finibus nisi in semper dictum.", "Nam at purus consequat, maximus erat sit amet, posuere risus.", "Proin pellentesque elit ut suscipit dictum.", "Quisque scelerisque nibh eget suscipit imperdiet.", "Nam non eros eget nisl molestie fringilla eget eu erat.", "Vivamus ut quam in ligula pellentesque tempor in eleifend elit.", "Nulla dictum est vitae elit egestas, et pharetra ligula dignissim.", "Praesent ut lorem eu ante pretium ultrices non vitae erat.", "Praesent maximus odio at libero bibendum, sit amet vehicula justo tempor.", "Curabitur ut mauris hendrerit, vehicula odio eget, luctus neque.", "Vestibulum eu ex varius, pellentesque ligula nec, rutrum leo.", "Aenean sed magna eget massa semper luctus sed sit amet tortor.", "Aenean eu dui in purus ornare egestas.", "Fusce sit amet diam porta neque porttitor aliquam.", "Proin a ipsum commodo, porta ligula non, fermentum augue.", "Morbi eget justo id diam mattis pellentesque in a erat.", "Duis vulputate tortor quis augue ultrices, in interdum purus interdum.", "Praesent aliquam quam tempus enim aliquet, in faucibus eros lobortis.", "Etiam auctor mi vitae augue suscipit pellentesque.", "Sed imperdiet nulla hendrerit justo tempus, vitae mollis turpis varius.", "Vivamus laoreet tellus at bibendum feugiat.", "Nullam et mauris placerat, porttitor nulla volutpat, aliquam sapien.", "Donec ac magna et est finibus dictum.", "Ut id tellus sit amet felis malesuada sollicitudin eget aliquet ligula.", "Donec vitae eros vel lorem aliquam rutrum.", "Duis vitae tellus ornare, pretium tellus et, condimentum sem."]
    part = BodyPart.objects.all()

    
    for index, value in enumerate(exercises):
        model = Exercises.objects.create(name=value, user=test_us, part=part[index])

def CreateRandomEx():
    test_us = User.objects.get(id=1)
    test_ex = Exercises.objects.all()
    
    id_test_ex = [ ex_id.id for ex_id in test_ex]
    for i in range(5):
        
        test_ex_instance = Exercises.objects.get(id=id_test_ex[0])
        test = UserExercise(user=test_us, exercise=test_ex_instance, reps=1, sets=1, kg=1, created=timezone.now() - timezone.timedelta(days=7))
        #UserExercise.objects.create(user=test_us, exercise=test_ex_instance, reps=1, sets=1, kg=1, created=timezone.now() - timezone.timedelta(days=i))
        test.save()