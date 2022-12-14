from django.shortcuts import render, redirect, get_object_or_404
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


def edit(request, id) -> str:
    data = get_object_or_404(Apps, pk=id)
    form = AppForms(instance=data)

    if request.method == 'POST':
        form = AppForms(request.POST, instance=data)

        if form.is_valid():
            data.save()
            return redirect('/')
        else:
            return render(request, 'edit.html', {'data': data})

    else:
        return render(request, 'edit.html', {'data': data})


def delete(request, id) -> str:
    data = get_object_or_404(Apps, pk=id)
    data.delete()
    return redirect('/')