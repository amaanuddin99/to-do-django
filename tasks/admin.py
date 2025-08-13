from django.contrib import admin
from .models import Task
class TaskAdmin(admin.ModelAdmin):
    list_display=("taskname","completed")
    search_fields=("taskname",)
admin.site.register(Task,TaskAdmin)
