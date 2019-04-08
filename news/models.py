from django.db import models
import uuid

# Create your models here.

class new(models.Model):
    id=models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    title=models.CharField(max_length=25,null=False)
    description=models.TextField(null=False)
    image=models.ImageField(blank=True,null=True,upload_to='images')
    createdAt=models.DateTimeField(auto_now=True)