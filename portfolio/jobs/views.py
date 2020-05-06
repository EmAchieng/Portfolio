from django.shortcuts import render
from .models import Job

# Create your views here.
def emily(request):
    jobs = Job.objects
    return render (request, 'Jobs/emily.html', {'jobs': jobs})
