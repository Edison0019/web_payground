from django.urls import path
from .views import ThreadDetail,ThreadList,add_message

urlpatterns = [
    path('', ThreadList.as_view(), name='message_list'),
    path('thread/<int:pk>/', ThreadDetail.as_view(), name='message_detail'),
    path('thread/<int:pk>/add',add_message,name='add')
]