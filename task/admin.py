from django.contrib import admin

# Register your models here.
from .models import Task
class TaskAdmin(admin.ModelAdmin):
        list_display = ('created_time','task_name','task_describe','task_host','task_command')

admin.site.register(Task, TaskAdmin)

