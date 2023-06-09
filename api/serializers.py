from rest_framework.serializers import ModelSerializer
from .models import Event

class EventSerializer(ModelSerializer):
    class Meta:
        model=Event
        fields=['id','event_name', 'data' ,'time', 'location' ,'image','is_liked']