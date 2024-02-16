from rest_framework import serializers
from . import models as m


class BookSerializer(serializers.ModelSerializer):

    class Meta:
        model = m.Book
        fields = '__all__'


class GrammarSerializer(serializers.ModelSerializer):
    class Meta:
        model = m.Grammar
        fields = '__all__'
