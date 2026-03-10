from django.conf import settings
from django.core import serializers
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from .forms import NewTableForm
from .models import IftarTable
import json

def home(request):
    tables = IftarTable.objects.all()
    tables_data = []
    for table in tables:
        tables_data.append({
            'title': table.title,
            'description': table.description,
            'lat': float(table.lat),
            'long': float(table.long),
        })

    context = {
        'api_key': settings.API_KEY,
        'tables': json.dumps(tables_data)
    }
    return render(request, 'home.html', context)

@login_required
def add_table(request):
    next_url = request.GET.get('next', '/')
    if request.method == 'POST':
        form = NewTableForm(request.POST) 
        if form.is_valid():   
            table = form.save(commit=False)  #بنحفظ مؤقتًا من غير ما يتسجل في الداتا بيز
            table.created_by = request.user
            table.save()

            return redirect(request.POST.get('next', next_url)) # عشان يرجع للصفحة اللي كان فيها
        else:
            print(form.errors)

    else:
        form = NewTableForm()
    
    context = {
        'api_key': settings.API_KEY,
        'form':form,
        'next':next_url,
    }

    return render(request,'add_table.html',context)
