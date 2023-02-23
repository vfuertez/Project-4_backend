from django.shortcuts import render
from .models import Info
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import InfoSerializer

# Create your views here.

class InfoViewSet(viewsets.ModelViewSet):
    queryset = Info.objects.all()
    serializer_class = InfoSerializer
    permission_classes = [permissions.AllowAny]
