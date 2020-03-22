#this is views for weather, all of the requests to the different links of the app will be dealt through this
from django.shortcuts import render

# Create your views here.
def home(request):
	return render(request,'home.html',{})

def about(request):
	return render(request,'about.html',{})