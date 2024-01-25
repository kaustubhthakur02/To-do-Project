from django.shortcuts import render, HttpResponse, redirect
from .models import Task,Login


# Create your views here.
def login(request): 
    if request.method == 'GET':
        return render(request, 'login.html')
    else:
        email = request.POST['email']
        password = request.POST['password']
        l = Login.objects.create(email=email, password= password)
        print(l)
        return redirect('/cr')


def create(request):
    if request.method == 'GET':
        return render(request, 'list1.html')
    else:
        task = request.POST['task']
        date = request.POST['date']
        priority = request.POST['priority']
        t = Task.objects.create(task=task, date=date, priority=priority)
        return redirect ('/sh')
    
def show(request):
    t = Task.objects.all()
    context = {
        "tasks": t
    }
    return render(request, "list2.html", context)

def delete(request,rid):
    t = Task.objects.filter(id = rid)
    t.delete()
    return redirect('/sh')

def edit(request,rid):
    if request.method == "GET":
        t = Task.objects.filter(id = rid)
        context = {}
        context["tasks"] = t
        return render(request, "list3.html", context)
    else:
        task = request.POST['task']
        date = request.POST['date']
        priority = request.POST['priority']
        t = Task.objects.filter(id = rid)
        t.update(task=task, date=date, priority=priority)
        return redirect ('/sh')


