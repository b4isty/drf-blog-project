from rest_framework import serializers

from .models import FriendRequest, Profile


class FriendRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = FriendRequest
        fields = '__all__'
        read_only_fields = ['from_user', ]


class AcceptIgnoreFriendRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['user', 'friends', 'avatar']
        read_only_fields = ['user', 'avatar']

    def create(self, validated_data):
        print(validated_data)





