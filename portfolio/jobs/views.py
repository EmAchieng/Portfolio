from django.shortcuts import render

# Create your views here.
def emily(request):
    return render (request, 'Jobs/emily.html')
