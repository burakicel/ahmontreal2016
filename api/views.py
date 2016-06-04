from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from api.models import Location
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
from rest_framework import status
from django.contrib.auth.models import User


# # Create your views here.
# class Test(APIView):
#     """
#     List all snippets, or create a new snippet.
#     """
#     def get(self, request, format=None):
#         return Response("sup dude")

# Create your views here.
class UpdateLocation(APIView):
    """
    List all snippets, or create a new snippet.
    """

    def post(self, request, format=None):
        location = Location.objects.get(user=(User.objects.get(username=request.data["user"])))
        location.longitude = request.data["longitude"]
        location.latitude = request.data["latitude"]
        location.save()
        return Response("OK", status=status.HTTP_200_OK)


updatelocation = UpdateLocation.as_view()