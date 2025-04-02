from django.shortcuts import render

def index(request):
    return render(request, 'APP/index.html')