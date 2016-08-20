from rest_framework import serializers

from .models import Choice, Question

class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
