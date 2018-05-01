from django.shortcuts import render
from django.views import generic

from .models import Zoo, Exhibit, Animal

# Create your views here.

def index(request):
	temporaryData = "Bill"
	return render(
		request,
		"index.html",
		context = { 'temporaryData' : temporaryData },
	)

class ZooDetailView(generic.DetailView):
    model = Zoo

class ExhibitDetailView(generic.DetailView):
    model = Exhibit

class AnimalDetailView(generic.DetailView):
    model = Animal
