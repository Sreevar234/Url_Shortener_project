from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from .models import *
import hashlib
from django.utils import timezone


class short_url_serializer(ModelSerializer):
    class Meta:
        model=short_url
        fields=['long_url']

    def create(self, validated_data):
        long=validated_data["long_url"]
        hash=hashlib.md5(long.encode('utf-8')).hexdigest()
        short=hash[:6]
        current_timestamp = timezone.now() 

        validated_data["short_code"]=short
        validated_data["created_at"]=current_timestamp.date()
        validated_data["updated_at"]=current_timestamp.date()
        return short_url.objects.create(**validated_data)

class update_url_serializer(serializers.ModelSerializer):
    class Meta:
        model=short_url
        fields="__all__"


    def update(self, instance, validated_data):
        long=validated_data["long_url"]
        hash=hashlib.md5(long.encode('utf-8')).hexdigest()
        short=hash[3:9]

        validated_data["short_code"]=short
        instance.save()
        return instance
        
class basic_serializer(ModelSerializer):
    class Meta:
        model=short_url
        fields="__all__"


