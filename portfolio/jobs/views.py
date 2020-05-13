from django.shortcuts import render
from .models import Job

# Create your views here.
def home(request):
    jobs = Job.objects
    return render (request, 'Jobs/home.html', {'jobs': jobs})
def detail(request, job_id):
    print(job_id)
    return render(request, 'Jobs/home.html')
