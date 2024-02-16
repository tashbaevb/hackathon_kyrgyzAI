import requests
from rest_framework.decorators import api_view

from rest_framework.response import Response
from rest_framework import status


@api_view(['POST'])
def text_to_speech(request):
    data = request.data
    data['speaker_id'] = 1

    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer lfRUZHFlLTht91Fg86AL1sVbcytXBs3vdhp17VTw2XA2a0pM5SAVWOr57KW4f3lL'
    }
    response = requests.post('http://tts.ulut.kg/api/tts/', json=data, headers=headers)

    if response.status_code == 200:
        return Response(response.json(), status=status.HTTP_200_OK)

    return Response({'error': 'Ошибка при отправке данных на другой backend'}, status=response.status_code)
