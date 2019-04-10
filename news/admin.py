from django.contrib import admin
from news.models import new
from boardmembers.models import member

# Register your models here.
class boardmembers(admin.ModelAdmin):
    list_display=('title','description')

class news(admin.ModelAdmin):
    list_display=('title','description','createdAt')
  
admin.site.register(new,news)
admin.site.register(member,boardmembers)

admin.site.site_header='Gara administration'
