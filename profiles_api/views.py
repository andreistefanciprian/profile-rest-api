from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response


# Create your views here.
class HelloApiView(APIView):
    """Test API View"""

    def get(self, request, format=None):
        """returns a list of APIView features"""

        an_apiview = [
            'Uses HTTP methods as function (get post patch delete)',
            'Similar to a traditional Django View',
            'Gives most control over app logic',
            'Mapped manually to URLs',
        ]

        return Response({'message': 'Hello!', 'an_apiview': an_apiview})