from django.contrib import admin
from .models import Todo

# Register your models here.
class TodoAdmin(admin.ModelAdmin):
    list_display = ['todoName', 'isCompleted', 'created', 'lastUpdated']
admin.site.register(Todo, TodoAdmin)