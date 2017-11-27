from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(['POST'])
def take_json_post(request):
    serializer = UserSerializer(data=request.data)
    return Response({'data': serializer})





from rest_framework import serializers
class UserSerializer(serializers.Serializer):

    username = serializers.CharField()
    password = serializers.CharField()

    def validate(self, data):
        username = data['username']
        password = data['password']

        return super(UserSerializer, self).validate(data)
