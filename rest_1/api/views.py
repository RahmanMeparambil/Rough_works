from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(['GET'])
def home(request):
    message  = {
        'nums':[1,2,3]
    }
    return Response(message)