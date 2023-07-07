from rest_framework import serializers
from .models import NoteEntity


class NoteEntitySerializer(serializers.ModelSerializer):
    class Meta:
        model = NoteEntity
        fields = '__all__'  # ['title', 'noteText']
