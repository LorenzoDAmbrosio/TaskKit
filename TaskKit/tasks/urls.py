from django.urls import path

from TaskKit import views
from TaskKit.views import login_view

urlpatterns = [
    path('', views.page_index, name='index'),
    path('communities/', views.page_communities, name='communities'),
    path('explore/', views.page_explore, name='explore'),
    path('login/', login_view, name='login'),
    path('account/', views.account_view, name='account'),
    path('account/edit/', views.edit_account_view, name='edit_account'),
    path('account/delete/', views.delete_account_view, name='delete_account'),
    path('logout/', views.logout_view, name='logout'),
    path('<str:page>/community/<int:community_id>/', views.community_detail, name='community_detail'),
    path('communities/project/<int:project_id>/', views.project_detail, name='project_detail'),

    path('task_create/project/<int:project_id>/', views.task_create, name='task_create'),
    path('task_update/project/<int:project_id>/task/<str:task_id>', views.task_update, name='task_update'),
    path('task_delete/task/<str:task_id>', views.task_delete, name='task_delete'),

    path('project_create/community/<int:community_id>', views.project_create, name='project_create'),
    path('project_update/community/<int:community_id>/project/<int:project_id>/', views.project_update, name='project_update'),
    path('project_delete/project/<int:project_id>', views.project_delete, name='project_delete'),

    path('status_delete/status/<int:status_id>', views.status_delete, name='status_delete'),
    path('status_create/project/<int:project_id>', views.status_create, name='status_create'),

]