from django.utils import timezone
from django.views.generic import DeleteView, UpdateView
from django.conf import settings
from django.core import serializers
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required
from .forms import NewTableForm
from .models import IftarTable
from django.utils.decorators import method_decorator
import json

def home(request):
    tables = IftarTable.objects.all()
    tables_data = []
    for table in tables:
        tables_data.append({
            'id': table.id,
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


def table_detail(request,table_id):
    table = get_object_or_404(IftarTable, id=table_id)
    context = {
        'api_key': settings.API_KEY,
        'table':table,
    }
    return render(request, 'table_detail.html',context)

@method_decorator(login_required,name='dispatch')  
class UpdateTable(UpdateView):
    model = IftarTable
    form_class = NewTableForm
    template_name = 'update_table.html'
    pk_url_kwarg = 'table_id'
    context_object_name = 'table'
    
    def get_queryset(self):
        return IftarTable.objects.filter(created_by=self.request.user)
    
    def form_valid(self, form):
        table = form.save(commit=False)
        table.updated_at = timezone.now()
        table.save()

        next_url = self.request.GET.get('next', '/')
        return redirect(next_url)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['api_key'] = settings.API_KEY  
        return context

@method_decorator(login_required, name='dispatch')
class DeleteTable(DeleteView):
    model = IftarTable
    pk_url_kwarg = 'table_id'

    def get_queryset(self):
        return IftarTable.objects.filter(created_by=self.request.user)

    def get(self, request, *args, **kwargs):
        table = self.get_object()
        table.delete()
        return redirect('/')
        