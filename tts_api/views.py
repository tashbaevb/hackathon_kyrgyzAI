from rest_framework.response import Response
from rest_framework import generics, permissions

from . import serializers as s


class TTSAPIView(generics.CreateAPIView):
    serializer_class = s.TTSSerializer
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, *args, **kwargs):
        pass