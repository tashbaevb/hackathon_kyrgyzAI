from rest_framework import serializers

from . import models as m


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = m.Course
        fields = '__all__'


class UserCourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = m.UserCourse
        fields = '__all__'

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['user_name'] = instance.user.username
        representation['course_name'] = instance.course.title
        return representation

