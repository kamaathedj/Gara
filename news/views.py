from django.shortcuts import render
from news.models import new

# Create your views here.
def newses():
    k= new.objects.order_by('-createdAt')
    news = []
    for news1 in k:
        data = {
            'id': news1.id,
            'title': news1.title,
            'description': news1.description,
            'image': news1.image,
            'createdAt':news1.createdAt
            
        }
        news.append(data)
   
    
   
    
    return  news
   
       