from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
# definir como función 
def index(request):
	return HttpResponse("Hola Mundo!")
