from django.contrib import admin
from tasks.models import Task  # Import the Task model from models.py

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'completed')
    search_fields = ('title',)
