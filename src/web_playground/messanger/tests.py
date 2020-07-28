from django.test import TestCase
from django.contrib.auth.models import User
from .models import Thread, Message
# Create your tests here.

class MessangerTest(TestCase):
    #this is the setup and is the place where
    #the attributes are initialized
    def setUp(self):
        self.user1 = User.objects.create_user('user1',None,'test1234')
        self.user2 = User.objects.create_user('user2',None,'test1234')

        self.thread = Thread.objects.create()

    def test_add_user(self):
        self.thread.users.add(self.user1,self.user2)
        self.assertEqual(len(self.thread.users.all()),2)

    def test_thread(self):
        self.thread.users.add(self.user2,self.user1)
        threads = Thread.objects.filter(users=self.user1).filter(users=self.user2)
        self.assertEqual(self.thread,threads[0])

    def test_non_thread(self):
        threads = Thread.objects.filter(users=self.user1).filter(users=self.user2)
        self.assertEqual(len(threads),0)

    def test_message_add(self):
        self.thread.users.add(self.user2,self.user1)
        message1 = Message.objects.create(user=self.user1,content='hola querido amigo')
        message2 = Message.objects.create(user=self.user2,content='hace mucho que no sabia de ti')
        self.thread.message.add(message1,message2)
        self.assertEqual(len(self.thread.message.all()),2)
        for m in self.thread.message.all():
            print('({}): {}'.format(m.user,m.content))