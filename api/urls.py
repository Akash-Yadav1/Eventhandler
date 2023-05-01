from django.urls import path,include
from . import views
urlpatterns = [

    path('',views.index,name='routes'),
    path('events/',views.getEvents,name='events'),
    path('events/<str:pk>',views.getEvent,name='event'),
    path('events/<str:pk>/update',views.updateEvents,name='updateevent'),
    path('liked/',views.getlikedEvent,name='likedevent')
]
