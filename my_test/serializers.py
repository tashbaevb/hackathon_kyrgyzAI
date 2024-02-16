from rest_framework import serializers
from . import models as m


class TestSerializer(serializers.ModelSerializer):

    class Meta:
        model = m.Test
        fields = '__all__'


class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = m.Question
        fields = '__all__'


class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = m.Answer
        fields = '__all__'
