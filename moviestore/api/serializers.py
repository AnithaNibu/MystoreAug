from rest_framework import serializers
from api.models import Movies
from django.contrib.auth.models import User
class MovieSerializer(serializers.Serializer):
    id=serializers.CharField(read_only=True)
    name=serializers.CharField()
    genre=serializers.CharField()
    director=serializers.CharField()
    release_date=serializers.DateField()
    number_of_shows=serializers.IntegerField()
    image=serializers.ImageField()
class MovieModelSerializer(serializers.ModelSerializer):
    class Meta:
        model=Movies
        fields="__all__"
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=["first_name","last_name","username","password","email"]
    def create(self, validated_data):
        return User.objects.create_user(**validated_data)

