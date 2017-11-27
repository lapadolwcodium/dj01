from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(['GET'])
def take_json(request):
    print('aaw dealer')
    dealer = request.GET.get('dealer')
    return Response({'data': dealer})
