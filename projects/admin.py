from django.contrib import admin
from projects.models import project

# Register your models here.
class projects(admin.ModelAdmin):
    list_display=('title','description','createdAt')
  
admin.site.register(project,projects)