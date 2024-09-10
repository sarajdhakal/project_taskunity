from django.urls import path
from .views import project_list, project_details, project_create,page_404,delete_project

urlpatterns = [
    path('project_list', project_list.project_list, name='project_list'),
    path('project_details/<id>/', project_details.project_details, name='project_details'),
    path('project_create', project_create.project_create, name='project_create'),
    path('page_404', page_404.page_404, name='page_404'),
    path('delete_project/<id>/', delete_project.delete_project, name = 'delete_project')
]