from rest_framework import serializers

from . import models as m


class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = m.Lesson
        fields = '__all__'


class UserLessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = m.UserLesson
        fields = '__all__'

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['user_name'] = instance.user.username
        representation['course_name'] = instance.lesson.title
        return representation


class ExampleSerializer(serializers.ModelSerializer):
    class Meta:
        model = m.Example
        fields = '__all__'

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['task_name'] = instance.task.title
        return representation


class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = m.Question
        fields = '__all__'


class TranslateSerializer(serializers.ModelSerializer):
    class Meta:
        model = m.Translate
        fields = '__all__'


class TTSSerializer(serializers.Serializer):
    text = serializers.CharField()
    speaker_id = serializers.IntegerField(default=1)
