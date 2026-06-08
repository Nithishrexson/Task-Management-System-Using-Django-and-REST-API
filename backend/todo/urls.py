from django.urls import path
from  .views import *

urlpatterns = [
    path('tasks/',tasks,name='tasks'),
    path('task/<int:pk>',task)
    
]