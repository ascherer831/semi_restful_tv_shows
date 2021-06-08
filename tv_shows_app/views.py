from django.shortcuts import render, redirect
from .models import Show

# Create your views here.

def root(request):
    return redirect('/shows')

def shows(request):
    context = {'all_shows': Show.objects.all()}
    
    return render(request, 'index.html', context)

def new(request):
    
    return render(request, 'new.html')

def create(request):
    this_show= Show.objects.create(title=request.POST['title'], network=request.POST['network'], release_date=request.POST['release_date'],description=request.POST['description'])
    return redirect(f'/shows/{this_show.id}')

def info(request,id):
    context = {'this_show':Show.objects.get(id=id)}

    return render(request, 'info.html',context)

def edit(request,id):
    context = {'this_show':Show.objects.get(id=id)}

    return render(request, 'edit.html', context)

def update(request, id):
    update_show = Show.objects.get(id=id)
    update_show.title = request.POST['title']
    update_show.network = request.POST['network']
    update_show.release_date = request.POST['release_date']
    update_show.description = request.POST['description']
    update_show.save()

    return redirect(f'/shows/{update_show.id}')

def delete(request,id):
    dead_show = Show.objects.get(id=id)
    dead_show.delete()
    return redirect ('/shows')

