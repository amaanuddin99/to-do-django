from django.urls import path
from . import views
urlpatterns=[path("addtask/",views.addtask,name="add_task"),
             path("removetask/<int:pk>/",views.removetask,name="removetask"),path("markdone/<int:pk>/",views.completed,name="done"),path("clear/",views.clearall,name='clear'),path("/edit/<int:pk>/",views.edit,name='editit')]