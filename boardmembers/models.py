from django.db import models
import uuid

# Create your models here.

class member(models.Model):
    id=models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    title=models.CharField(max_length=25,null=False)
    description=models.TextField(null=False)
    person=models.ImageField(blank=True,null=True,upload_to='persons')

    def __str__(self):
        return self.title
    class Meta:
        verbose_name_plural="members"


