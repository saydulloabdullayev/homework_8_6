from rest_framework import viewsets

from app_figma.models import Add
from app_figma.serializers import  AddDetailSerializer

class AddViewSet(viewsets.ModelViewSet):
    queryset = Add.objects.all()
    serializer_class = AddDetailSerializer

