from django.contrib.auth.models import User
from rest_framework import serializers
from .models import GenericFileUpload, Marketting, MarkettingBanners


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ("username", "email", "date_joined",)


class GenericFileSerializer(serializers.ModelSerializer):

    class Meta:
        model = GenericFileUpload
        fields = "__all__"


class MarkettingBannerSerializer(serializers.ModelSerializer):
    marketting = serializers.CharField(read_only=True)
    marketting_id = serializers.IntegerField(write_only=True)

    class Meta:
        model = MarkettingBanners
        fields = "__all__"


class MarkettingSerializer(serializers.ModelSerializer):
    banners = MarkettingBannerSerializer(read_only=True, many=True)

    class Meta:
        model = Marketting
        fields = "__all__"
