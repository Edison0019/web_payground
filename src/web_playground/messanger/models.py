from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import m2m_changed
from django.utils import timezone

# Create your models here.
class Message(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,)
    content = models.TextField(verbose_name='Message')
    # active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['created']

#this is a class for defining our custom model managers
class ThreadManager(models.Manager):
    def find(self,user1,user2):
        #as you can see the self p arameter represents the query set of all the instances of the model
        queryset = self.filter(users=user1).filter(users=user2)
        if len(queryset) > 0:
            return queryset[0]
        else:
            return None
    
    def find_or_create(self,user1,user2):
        #as you can see the self p arameter represents the query set of all the instances of the model
        queryset = self.find(user1,user2)
        if queryset is None:
            queryset = self.create()
            queryset.users.add(user1,user2)
            return queryset
        else:
            return queryset


class Thread(models.Model):
    users = models.ManyToManyField(User,related_name='threads')
    message = models.ManyToManyField(Message)

    objects = ThreadManager()

def message_change(sender,**kwargs):
    instance = kwargs.pop('instance',None)
    action = kwargs.pop('action',None)
    pk_set = kwargs.pop('pk_set',None)
    print(instance,action,pk_set)

    #this is creating a set of elements to add not allowed messages
    not_allowed_messages = set()
    if action is 'pre_add':
        for msg_pk in pk_set:
            msg = Message.objects.get(pk=msg_pk)
            if msg.user not in  instance.users.all():
                print('Ups, ({}) is not part of this thread'.format(msg.user))
                not_allowed_messages.add(msg_pk)

    #this part deletes the not allowed messages from pk.set using a python built in method
    pk_set.difference_update(not_allowed_messages)

m2m_changed.connect(message_change,sender=Thread.message.through)