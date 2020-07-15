from django.urls import path
from .views import PageDetail,PageListView,PageCreate

pages_patterns = ([
    path('', PageListView.as_view(), name='pages'),
    path('<int:pk>/<slug:slug>/', PageDetail.as_view(), name='page'),
    path('create/',PageCreate.as_view(),name='create'),
],'pages')