from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Message(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,)
    content = models.TextField(verbose_name='Message')
    # active = models.BooleanField(default=True)
    created = models.DateField(auto_now_add=True,verbose_name='date')

    class Meta:
        ordering = ['created']
        
class Thread(models.Model):
    users = models.ManyToManyField(User,related_name='threads')
    message = models.ManyToManyField(Message)