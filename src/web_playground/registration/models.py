from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

#custom function to delete the current picture before using another one
def delete_old_picture(instance,filename):
    old_instance = Profile.objects.get(pk=instance.pk)
    old_instance.avatar.delete()
    return 'profile/' + filename

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models .CASCADE)
    avatar = models.ImageField(upload_to=delete_old_picture,null=True,blank=True)
    bio = models.TextField(null=True,blank=True)
    link = models.URLField(null=True,blank=True,max_length=200)
    def __str__(self):
        return str(self.user)

    class Meta:
        ordering = ['user__username']

@receiver(post_save,sender=User)
def profile_creation_signal(sender,instance, **kwargs):
    if kwargs.get('created',False): #this to make sure that the action is executed the first time the instance is created
        Profile.objects.get_or_create(user=instance)
        print('profile created for the current instance')