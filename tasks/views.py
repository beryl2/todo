from asyncio import tasks
from django.shortcuts import render, redirect
from django.http import HttpResponse

from .models import *
from .forms import *


# Create your views here.
def index(request):
    tasks= Task.objects.all()

    form = TaskForm()

    if request.method =='POST':
        form = TaskForm(request.POST)
        if form.is_valid():    #this will save it to the database
            form.save()
        return redirect('/')    



    context = {'tasks':tasks, 'form':form}
    return render(request, 'tasks/list.html', context)

def updateTask(request, pk):
    task = Task.objects.get(id = pk) #this view will bwe dynamic and have a dynamic url path 
    return render(request, 'tasks/update_task.html')
