from django.urls import path
from .views import *

urlpatterns = [
    path('home/',home,name='home'),
    path('add/',add,name='add'),
    path('complete/',complete,name='complete'),
    path('trash/',trash,name='trash'),
    path('about/',about,name='about'),
    path('support/',support,name='support'),
    path('update/<int:pk>',update,name ='update'),
    path('delete/<int:pk>',delete,name ='delete')
    
]
