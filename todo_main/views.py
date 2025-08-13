from django.shortcuts import render
from tasks.models import Task
def home(request):
    todotasks=Task.objects.filter(completed=False)
    donetasks=Task.objects.filter(completed=True)
    context={"completed":donetasks,"tocomplete":todotasks}

  
    
    
    return render(request,'home.html',context)