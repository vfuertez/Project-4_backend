from .models import Info
from rest_framework import serializers

class InfoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        
        model = Info
        
        fields = ['id', 'name', 'link1', 'link2', 'web']