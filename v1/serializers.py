from django.contrib.auth.models import User, Group
from rest_framework import serializers
from v1.models import Course, Game, Hole, Score

class UserSerializer(serializers.HyperlinkedModelSerializer):
    def create(self, validated_data):
        return User.objects.create(**validated_data)

    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')

class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')

class CourseSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Course
        fields = ('name', 'holes', 'address')

class GameSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Game
        fields = ('players', 'date', 'scores', 'course')

class HoleSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Hole
        fields = ('number', 'yardage', 'par')

class ScoreSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Score
        fields = ('player', 'hole', 'total')
