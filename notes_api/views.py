from rest_framework import generics
from .models import NoteEntity
from .serializer import NoteEntitySerializer

# Create your views here.
# get post update delete


class NoteEntityGet(generics.ListCreateAPIView):
    queryset = NoteEntity.objects.all()
    serializer_class = NoteEntitySerializer


class NoteEntityUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
    queryset = NoteEntity.objects.all()
    serializer_class = NoteEntitySerializer
