from rest_framework import serializers
from . import models as m


class DictationSerializer(serializers.ModelSerializer):

    class Meta:
        model = m.Dictation
        fields = '__all__'


class SentenceSerializer(serializers.ModelSerializer):

    class Meta:
        model = m.Sentence
        fields = '__all__'


class WordSerializer(serializers.ModelSerializer):

    class Meta:
        model = m.Word
        fields = '__all__'
