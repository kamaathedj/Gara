from django.shortcuts import render
from projects.models import project
from news.views import newses
from boardmembers.views import boardmember

def projects(request):
    k= project.objects.order_by('-createdAt')
    projects = []
    for projo in k:
        data = {
            'id': projo.id,
            'title': projo.title,
            'description': projo.description,
            'image': projo.image,
            'createdAt':projo.createdAt
            
        }
        projects.append(data)
    
    news=newses()
    member=boardmember()
    
    context={'projects':projects,'news':news,'member':member}
    
    
    
    
   

    return render(request,'temps/index.html',context)
   
       

