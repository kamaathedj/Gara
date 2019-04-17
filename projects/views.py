from django.shortcuts import render
from projects.models import project

def projects(request):
    k= project.objects.order_by('-createdAt')
    projects = []
    for projo in k:
        prog = {
            'id': projo.id,
            'title': projo.title,
            'description': projo.description,
            'image': projo.image,
            'createdAt':projo.createdAt
            
        }
        projects.append(prog)
    context={'projects':projects}
    print(context)

    return render(request,'temps/index.html',context)
   
       

