from django.shortcuts import render
from rest_framework import viewsets
from .models import UserOfSecondApp as CoolUsers
from .serializers import CoolSerialzer
from rest_framework.response import Response

class CoolUsersAPI(viewsets.ModelViewSet):
    queryset = CoolUsers.objects.all()
    serializer_class = CoolSerialzer
    print('Cool')
    def create(self, request):
        ##has to be changed is not working
        return Response(status=200)

