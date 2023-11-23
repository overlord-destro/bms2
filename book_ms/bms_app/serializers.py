from rest_framework import serializers
from .models import Books, Accessor
import datetime


class BooksSerializer(serializers.Serializer):        
    title = serializers.CharField(max_length=100)
    author = serializers.CharField(max_length=50)
    pub_year = serializers.CharField(max_length=4)

    def create(self, validated_data):
        return Books.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.author = validated_data.get('author', instance.author)
        instance.pub_year = validated_data.get('pub_year', instance.pub_year)

        instance.save()
        return instance


class AccessorSerializer(serializers.Serializer):
    book_title = serializers.CharField(max_length=100)
    name = serializers.CharField()
    mail = serializers.CharField()
    date_checked_out = serializers.DateTimeField()

    def create(self, validated_data):
        return Accessor.objects.create(**validated_data)
