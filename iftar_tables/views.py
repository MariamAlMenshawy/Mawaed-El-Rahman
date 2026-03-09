from django.conf import settings
from django.shortcuts import render

# Create your views here.

def home(request):
    context = {
        'api_key': settings.API_KEY
    }
    return render(request,'home.html',context)
