
from rest_framework.permissions import IsAuthenticated 
from rest_framework.generics import (
    ListAPIView,
    RetrieveAPIView,
    CreateAPIView,
    DestroyAPIView, 
    RetrieveUpdateAPIView,
)

from django_filters import rest_framework as filters

from .models import Add, News
from .serializers import AddDetailSerializer, AddSerializer


class AddFilter(filters.FilterSet):
    name = filters.CharFilter(lookup_expr='icontains', field_name='nomi')

class AddListAPIView(ListAPIView):
    queryset = Add.objects.all()
    serializer_class = AddSerializer
    filter_backends = [filters.DjangoFilterBackend]
    filterset_class = AddFilter


    def get_queryset(self):
        if 'keyword' in self.request.query_params:
            return Add.objects.filter(nomi__icontains= self.request.query_params['keyword'])
        return Add.objects.all()


class AddDetailAPIView(RetrieveAPIView):
    queryset = Add.objects.all()
    serializer_class = AddDetailSerializer


class AddCreateAPIView(CreateAPIView):
    queryset = Add.objects.all()
    serializer_class = AddDetailSerializer
    permission_classes = [IsAuthenticated]

class AddDeleteAPIView(DestroyAPIView):
    queryset = Add.objects.all()
    serializer_class = AddDetailSerializer

class AddUpdateAPIView(RetrieveUpdateAPIView):
    queryset = Add.objects.all()
    serializer_class = AddDetailSerializer






