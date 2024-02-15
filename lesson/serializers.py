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
