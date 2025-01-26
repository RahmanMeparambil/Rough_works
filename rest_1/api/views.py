from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import PersonSerializer, Person


@api_view(['GET'])
def home(request):
    persons = Person.objects.all()
    serializer = PersonSerializer(persons, many=True)
    return Response(serializer.data)