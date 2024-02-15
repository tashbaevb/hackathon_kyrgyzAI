from rest_framework import serializers

from . import models as m


class TaskSerializer(serializers.ModelSerializer):

    class Meta:
        model = m.Task
        fields = '__all__'

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['lesson_name'] = instance.lesson.title
        return representation


class ExampleSerializer(serializers.ModelSerializer):

    class Meta:
        model = m.Example
        fields = '__all__'

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['task_name'] = instance.task.title
        return representation
