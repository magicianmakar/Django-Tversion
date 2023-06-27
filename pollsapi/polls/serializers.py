from rest_framework import serializers
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from .models import Poll, Choice, Vote


class VoteSerializers(serializers.ModelSerializer):
    class Meta:
        model = Vote
        fields = "__all__"


class ChoiceSerializers(serializers.ModelSerializer):
    votes = VoteSerializers(many=True, required=False)

    class Meta:
        model = Choice
        fields = "__all__"


class PollSerializers(serializers.ModelSerializer):
    choices = ChoiceSerializers(many=True, read_only=True, required=False)

    class Meta:
        model = Poll
        fields = "__all__"


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ("username", "email", "password")
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        user = User(email=validated_data["email"], username=validated_data["username"])
        user.set_password(validated_data["password"])
        user.save()
        Token.objects.create(user=user)
        return user
