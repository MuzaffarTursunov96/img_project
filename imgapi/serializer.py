from rest_framework import serializers

from .models import UserImage 

class UserImageListSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserImage
        fields = ['id','image']


class UserImagePostSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserImage
        fields = ['image','meta_name','meta_geolocation','meta_description']

class UserImageNameSerializer(serializers.ModelSerializer):
  class Meta:
    model=UserImage
    fields =['meta_name']

class UserImageDetailSerializer(serializers.ModelSerializer):
  class Meta:
    model=UserImage
    fields =['id','image','meta_name','meta_geolocation','meta_description']