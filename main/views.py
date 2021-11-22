from django.shortcuts import render
from .models import Person
# Create your views here.


def person_view(request, person_id):
    peep = Person.objects.get(id=person_id)
    return render(request, 'person.html', {'person': peep})


def people_view(request):
    people = Person.objects.all().order_by('age')
    return render(request, 'people.html', {'my_people': people})
