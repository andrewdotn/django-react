from rest_framework import serializers

from .models import Choice, Question

class ChoiceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Choice

class QuestionSerializer(serializers.HyperlinkedModelSerializer):
    choice_set = ChoiceSerializer(many=True)

    class Meta:
        model = Question
