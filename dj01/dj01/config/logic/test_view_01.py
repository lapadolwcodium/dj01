from rest_framework.response import Response
from rest_framework.views import APIView

from rest_framework import viewsets

class ListUsers(viewsets.ViewSet):
    def list(self, request):
        print('sssqq')
        return Response({'user': 'dq snippet_list'})

