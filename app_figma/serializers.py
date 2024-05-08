from rest_framework import serializers

from .models import Add, News

class AddSerializer(serializers.ModelSerializer):
    add_detail_url = serializers.SerializerMethodField(read_only=True, source = 'get_add_detail_url')
    class Meta:    
        model = Add
        fields = ['id','nomi', 'yil', 'add_detail_url']


    def get_add_detail_url(self, obj):
        return f'http://127.0.0.1:8000/api/v1/add/{obj.id}'


class AddDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Add
        fields = '__all__'

