from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Event
from .serializers import EventSerializer
# Create your views here.

@api_view(['GET'])
def index(request):
    routes = [
        {
            'Endpoint': '/events/',
            'method': 'GET',
            'body': None,
            'description': 'Returns an array of events'
        },
        {
            'Endpoint': '/events/id',
            'method': 'GET',
            'body': None,
            'description': 'Returns a single event object'
        },
        {
            'Endpoint': '/events/create/',
            'method': 'POST',
            'body': {'body': ""},
            'description': 'Creates new event with data sent in post request'
        },
        {
            'Endpoint': '/notes/id/update/',
            'method': 'PUT',
            'body': {'body': ""},
            'description': 'Creates an existing note with data sent in post request'
        },
        {
            'Endpoint': '/events/id/delete/',
            'method': 'DELETE',
            'body': None,
            'description': 'Deletes an exiting event'
        },
    ]
    return Response(routes)

@api_view(['GET'])
def getEvents(request):
    events=Event.objects.all()
    serializer=EventSerializer(events,many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getEvent(request,pk):
    event=Event.objects.get(id=pk)
    serializer=EventSerializer(event,many=False)
    return Response(serializer.data)

@api_view(['GET'])
def getlikedEvent(request):
    event=Event.objects.all()
    serializer=EventSerializer(event,many=True)
    liked=[]
    for i in serializer.data:
            if i['is_liked']==True:
                liked.append(i)
    return Response(liked)

# @api_view(['PUT'])
# def updateEvents(request,pk):
#      data=request.data
#      event=Event.objects.get(id=pk)
#      serializer=EventSerializer(instance=event,many=False)
#      if serializer.is_valid():
#           serializer.save()

#      return Response(serializer.data)

@api_view(['PUT'])
def updateEvents(request,pk):
     event=Event.objects.all()
     serializer=EventSerializer(instance=event,many=False)
     liked=[]
     for i in serializer.data:
            if i['is_liked']==True:
                i['is_liked']=False
     return Response(liked)
