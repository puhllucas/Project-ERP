from django.shortcuts import render, redirect
from .models import Apps
from .forms import AppForms

def home(request):
    data = Apps.objects.all()
    
    if request.method == 'POST':
        form = AppForms(request.POST)

        if form.is_valid():
            app = form.save(commit=False)
            app.save()
            return redirect('/')
        
        else:
            form = AppForms()
            
    return render(request, 'index.html', {'data': data})
