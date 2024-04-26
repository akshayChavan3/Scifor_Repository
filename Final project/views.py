from rest_framework import generics
from .models import YourCorrectEventModelName  # Replace YourCorrectEventModelName with the correct name of your model
from .serializers import EventSerializer

class EventList(generics.ListAPIView):
    queryset = YourCorrectEventModelName.objects.all()  # Replace YourCorrectEventModelName with the correct name of your model
    serializer_class = EventSerializer
