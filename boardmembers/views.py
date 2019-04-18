from django.shortcuts import render

# Create your views here.
from boardmembers.models import member

# Create your views here.
def boardmember():
    k= member.objects.order_by('-id')
    members = []
    for bom in k:
        data = {
            'id': bom.id,
            'title': bom.title,
            'description': bom.description,
            'image': bom.person,
            
        }
        members.append(data)
    
    return  members
   
       