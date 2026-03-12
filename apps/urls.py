
from django.urls import path 
from .views import project, projects , projects_add, projects_edit, projects_delete

urlpatterns = [
    path('', project, name="project"),
    path('project/', project, name="project"),
    path('project_add/', projects_add, name="project_add"),
    path('project_edit/<uuid:id>/', projects_edit, name="project_edit"),
    path('project_delete/<uuid:id>/', projects_delete, name="project_delete"),
    path('projects/<uuid:id>/', projects, name="projects"),
]
 