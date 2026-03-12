from django.contrib import messages
from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .models import Project
from .forms import ProjectForm

# def project(request):
    
#     reviews_p = Review.objects.filter(value='+')
#     reviews_m = Review.objects.filter(value='-')
#     project = Project.objects.filter(project_review__isnull=True)
#     context = {
#         'reviews_p':reviews_p,
#         'reviews_m':reviews_m,
#         "project":project
#     }
#     return render(request, "project/project.html",context)
def project(request):
    project = Project.objects.all()
    context = {
        "project":project
    }
    return render(request, "project/project.html",context)
    
# def projects(request, id):
#     projects = Project.objects.get(id=id)
#     tag = Tag.objects.all()
#     context = {
#         "projects":projects,
#         "tag":tag
#     }
#     return render(request, "project/projects.html", context)

def projects(request, id):
    try:
        projects = Project.objects.get(id=id)
    except Project.DoesNotExist:
        messages.warning(request,'xato berdi')
        return redirect('project')
    context = {
        "projects":projects
    }
    return render(request, "project/projects.html", context)

@login_required(login_url='login')
def projects_add(request,):
    if request.method == 'POST':
        project_form = ProjectForm(request.POST,request.FILES)
        if project_form.is_valid():
            project = project_form.save(commit=False)
            project.user = request.user.profil
            project.save()
            return redirect('project')
        
    project_form = ProjectForm()
    context = {
        'form':project_form
    }
    return render(request, "project/project_add.html", context)


@login_required(login_url='login')
def projects_edit(request, id):
    project = Project.objects.get(id=id)
    project_form = ProjectForm(instance=project)
    if request.method == 'POST':
        project_form = ProjectForm(request.POST,request.FILES,instance=project)
        if project_form.is_valid():
            project_form.save()
            return redirect('project')
        
    context = {
        'form':project_form
    }
    return render(request, "project/project_add.html", context)

@login_required(login_url='login')
def projects_delete(request, id):
    profil = request.user.profil
    try:
        profil.project_set.get(id=id)
    except Project.DoesNotExist:
        messages.warning(request,"Sizda faqat o'zingiz uchun loyihalargiz Delete  olasizmi ")
        return redirect('project')
    
    project = Project.objects.get(id=id)
    project.delete()
    return redirect('project')