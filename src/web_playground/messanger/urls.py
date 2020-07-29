from django.urls import path
from .views import ThreadDetail,ThreadList

urlpatterns = [
    path('', ThreadList.as_view(), name='message_list'),
    path('thread/<int:pk>/', ThreadList.as_view(), name='message_detail'),
]