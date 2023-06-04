from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Project, Task
from django.shortcuts import get_object_or_404, render

# Create your views here.

def index( request ):
    # return HttpResponse("Index Page")
    return render( request , 'index.html')

def hello( request, username ):
    return HttpResponse("<h1>Hola %s</h1>" % username)

def about( request ):
    # return HttpResponse('About')
    user = 'new user'
    return render(request, 'about.html', {
        'user': user
    })

def projects( request ):
    # projects = list(Project.objects.values())
    # return JsonResponse(projects, safe = False)
    projects = Project.objects.all();
    return render(request, 'projects.html', {
        'projects': projects 
    })

def tasks( request ):
    # task = Task.objects.get( id = id )
    # task = get_object_or_404(Task, id = id)
    # return HttpResponse('task: %s' % task.title)
    tasks = Task.objects.all()
    return render( request, 'tasks.html', {
       'tasks' : tasks 
    })