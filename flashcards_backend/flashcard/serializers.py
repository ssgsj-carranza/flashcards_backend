from rest_framework import serializers
from .models import Flashcard


class FlashcardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Flashcard
        fields = ['id', 'flashcard_title', 'flashcard_word', 'flashcard_definition', 'collection_id']