from rest_framework.parsers import MultiPartParser
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import (
    ListAPIView,
    RetrieveAPIView,
    CreateAPIView,
    DestroyAPIView, 
    RetrieveUpdateAPIView,
)

from django_filters import rest_framework as filters
from .models import Add, News, Management, Structura, Electronic_Fund, Contact, Building
from .serializers import (
    AddDetailSerializer, 
    AddSerializer,
    NewsSerializer, 
    NewsDetailSerializer, 
    ManagementSerializer, 
    ManagementDetailSerializer,
    StructuraSerializer,
    StructuraDetailSerializer,
    ElectronicFundSerializer,
    BuildingSerializer,
    ContactSerializer,
)


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



class NewsFilter(filters.FilterSet):
    name = filters.CharFilter(lookup_expr='icontains', field_name='nomi')

class NewsListAPIView(ListAPIView):
    queryset = News.objects.all()
    serializer_class = NewsSerializer
    filter_backends = [filters.DjangoFilterBackend]
    filterset_class = NewsFilter


    def get_queryset(self):
        if 'keyword' in self.request.query_params:
            return News.objects.filter(nomi__icontains= self.request.query_params['keyword'])
        return News.objects.all()


class NewsDetailAPIView(RetrieveAPIView):
    queryset = News.objects.all()
    serializer_class = NewsDetailSerializer


class NewsCreateAPIView(CreateAPIView):
    queryset = News.objects.all()
    serializer_class = NewsDetailSerializer
    permission_classes = [IsAuthenticated]

class NewsDeleteAPIView(DestroyAPIView):
    queryset = News.objects.all()
    serializer_class = NewsDetailSerializer

class NewsUpdateAPIView(RetrieveUpdateAPIView):
    queryset = News.objects.all()
    serializer_class = NewsDetailSerializer



class ManagementFilter(filters.FilterSet):
    name = filters.CharFilter(lookup_expr='icontains', field_name='nomi')

class ManagementListAPIView(ListAPIView):
    queryset = Management.objects.all()
    serializer_class = ManagementSerializer
    filter_backends = [filters.DjangoFilterBackend]
    filterset_class = ManagementFilter


    def get_queryset(self):
        if 'keyword' in self.request.query_params:
            return Management.objects.filter(nomi__icontains= self.request.query_params['keyword'])
        return Management.objects.all()


class ManagementDetailAPIView(RetrieveAPIView):
    queryset = Management.objects.all()
    serializer_class = ManagementDetailSerializer


class ManagementCreateAPIView(CreateAPIView):
    queryset = Management.objects.all()
    serializer_class = ManagementDetailSerializer
    permission_classes = [IsAuthenticated]

class ManagementDeleteAPIView(DestroyAPIView):
    queryset = Management.objects.all()
    serializer_class = ManagementDetailSerializer

class ManagementUpdateAPIView(RetrieveUpdateAPIView):
    queryset = Management.objects.all()
    serializer_class = ManagementDetailSerializer



class StructuraFilter(filters.FilterSet):
    name = filters.CharFilter(lookup_expr='icontains', field_name='nomi')

class StructuraListAPIView(ListAPIView):
    queryset = Structura.objects.all()
    serializer_class = StructuraSerializer
    filter_backends = [filters.DjangoFilterBackend]
    filterset_class = StructuraFilter


    def get_queryset(self):
        if 'keyword' in self.request.query_params:
            return Structura.objects.filter(nomi__icontains= self.request.query_params['keyword'])
        return Structura.objects.all()


class StructuraDetailAPIView(RetrieveAPIView):
    queryset = Structura.objects.all()
    serializer_class =StructuraDetailSerializer


class StructuraCreateAPIView(CreateAPIView):
    queryset = Structura.objects.all()
    serializer_class = StructuraDetailSerializer
    permission_classes = [IsAuthenticated]

class StructuraDeleteAPIView(DestroyAPIView):
    queryset = Structura.objects.all()
    serializer_class = StructuraDetailSerializer

class StructuraUpdateAPIView(RetrieveUpdateAPIView):
    queryset =Structura.objects.all()
    serializer_class =StructuraDetailSerializer



class ElectronicFundViewSet(ListAPIView):
    queryset = Electronic_Fund.objects.all()
    serializer_class = ElectronicFundSerializer
    permission_classes = [MultiPartParser]


class ContactViewSet(ListAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
    permission_classes = [MultiPartParser]


class BuildingViewSet(ListAPIView):
    queryset = Building.objects.all()
    serializer_class = BuildingSerializer
    permission_classes = [MultiPartParser]