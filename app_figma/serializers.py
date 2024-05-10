from rest_framework import serializers

from .models import Add, News, Management, Structura

class AddSerializer(serializers.ModelSerializer):
    add_detail_url = serializers.SerializerMethodField(read_only=True, source = 'get_add_detail_url')
    class Meta:    
        model = Add
        fields = ['id','nomi', 'add_detail_url']


    def get_add_detail_url(self, obj):
        return f'http://127.0.0.1:8000/api/v1/add/{obj.id}'


class AddDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Add
        fields = '__all__'


class NewsSerializer(serializers.ModelSerializer):
    news_detail_url = serializers.SerializerMethodField(read_only=True, source = 'get_news_detail_url')
    class Meta:    
        model = News
        fields = ['id','title', 'news_detail_url']


    def get_news_detail_url(self, obj):
        return f'http://127.0.0.1:8000/api/v1/news/{obj.id}'


class NewsDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = '__all__'


class ManagementSerializer(serializers.ModelSerializer):
    management_detail_url = serializers.SerializerMethodField(read_only=True, source = 'get_management_detail_url')
    class Meta:    
        model = Management
        fields = ['id','name', 'number', 'news_detail_url']


    def get_management_detail_url(self, obj):
        return f'http://127.0.0.1:8000/api/v1/management/{obj.id}'


class ManagementDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Management
        fields = '__all__'


class StructuraSerializer(serializers.ModelSerializer):
    structura_detail_url = serializers.SerializerMethodField(read_only=True, source = 'get_management_detail_url')
    class Meta:    
        model = Structura
        fields = ['id','title', 'name', 'news_detail_url']


    def get_structura_detail_url(self, obj):
        return f'http://127.0.0.1:8000/api/v1/structura/{obj.id}'


class StructuraDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Structura
        fields = '__all__'

