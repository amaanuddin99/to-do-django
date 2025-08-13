from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from . import models
from django import forms
from django.contrib import messages

def addtask(request):
    if(request.POST["task"]==""):
          messages.error(request, "Task name cannot be empty.")
          return redirect(to='home')

    
    models.Task(request.POST["task"])
    models.Task.objects.create(taskname=request.POST["task"])
    
    return redirect(to="home")
def removetask(request,pk):
    task=get_object_or_404(models.Task,pk=pk)
    task.delete()
    return redirect(to="home")
def completed(request,pk):
    task=get_object_or_404(models.Task,pk=pk)
    task.completed=True
    task.save()
    return redirect(to="home")
def clearall(request):
    all=models.Task.objects.filter(completed=True)
    all.delete()
    return redirect(to="home")
def edit(request,pk):
    task=get_object_or_404(models.Task,pk=pk)
    context={
        'task':task
    }
    if(request.method=='POST'):
        if(request.POST["task"]==""):
          messages.error(request, "Task name cannot be empty.")
          return redirect(to='home')
        task.taskname=request.POST["task"]
        task.save()
        return redirect(to='home')
    else:
        return render(request,'task.html',context)

