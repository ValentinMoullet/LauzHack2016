from django.shortcuts import render

def index(request):
	return render(request, 'LauzHackApp/seeThroughMe.html')

# Create your views here.
