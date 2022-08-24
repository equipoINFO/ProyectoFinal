from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
# definir como función 
def index(request):
	return render(request, 'nosotros.html')

#def nosotros(request):
   # return render(request, 'nosotros.html')

#def base(request):
  #  return render(request, 'base.html')
