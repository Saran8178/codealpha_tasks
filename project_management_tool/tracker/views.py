from django.shortcuts import render, get_object_or_404
from .models import Project, Task
def index(request):
    projects = Project.objects.all()
    return render(request, 'tracker/index.html', {'projects': projects})
def project_detail(request, project_id):
    project = get_object_or_404(Project, pk=project_id)
    tasks = project.task_set.all()
    return render(request, 'tracker/project_detail.html', {'project': project, 'tasks': tasks})
