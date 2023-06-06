from django.shortcuts import render
from .models import Task
# Create your views here.
def home(request):
    context={'success':False}
    if request.method == "POST":
        title=request.POST.get('title')
        desc=request.POST.get('desc')
        ins=Task(taskTitle=title, taskDesc=desc)
        ins.save()
        context={'success':True}
    return render(request,'index.html',context)

def task(request):
    allTasks=Task.objects.all()
    context={'tasks':allTasks}
    return render(request,'task.html',context)
