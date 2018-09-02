from django.contrib.auth.models import User, Group
from rest_framework import serializers
from v1.models import Course, Game, Hole, Score

class UserSerializer(serializers.HyperlinkedModelSerializer):
    def create(self, validated_data):
        return User.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.username = validated_data.get('username', instance.username)
        instance.email = validated_data.get('email', instance.email)
        instance.save()
        return instance

    class Meta:
        model = User
        fields = ('id', 'url', 'username', 'email')

class GroupSerializer(serializers.HyperlinkedModelSerializer):
    def create(self, validated_data):
        return Group.objects.create(**validated_data)

    class Meta:
        model = Group
        fields = ('id', 'url', 'name')

class CourseSerializer(serializers.HyperlinkedModelSerializer):
    def create(self, validated_data):
        course = Course.objects.create()
        course.name = validated_data.get('name', course.name)
        course.address = validated_data.get('address', course.address)
        course.length = validated_data.get('length', course.length)

        while course.holes.count() < course.length:
            number = course.holes.count() + 1
            hole = Hole.objects.create(course=course, number=number)
            course.holes.add(hole)

        course.save()
        return course

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.address = validated_data.get('address', instance.address)
        instance.length = validated_data.get('length', instance.length)
        holes = validated_data.get('holes', instance.holes)
        instance.holes.set(holes)
        instance.save()
        return instance

    class Meta:
        model = Course
        fields = ('id', 'url', 'name', 'holes', 'address', 'length')

class GameSerializer(serializers.HyperlinkedModelSerializer):
    def create(self, validated_data):
        # game.name = validated_data.get('name', game.name)
        # game.address = validated_data.get('address', game.address)
        # game.length = validated_data.get('length', game.length)
        return Game.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.players = validated_data.get('players', instance.players)
        instance.date = validated_data.get('date', instance.date)
        instance.scores = validated_data.get('scores', instance.scores)
        instance.course = validated_data.get('course', instance.course)
        instance.save()
        return instance

    class Meta:
        model = Game
        fields = ('id', 'players', 'date', 'scores', 'course')

class HoleSerializer(serializers.HyperlinkedModelSerializer):
    def create(self, validated_data):
        return Hole.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.number = validated_data.get('number', instance.number)
        instance.yardage = validated_data.get('yardage', instance.yardage)
        instance.par = validated_data.get('par', instance.par)
        instance.save()
        return instance

    class Meta:
        model = Hole
        fields = ('id', 'course', 'number', 'yardage', 'par')

class ScoreSerializer(serializers.HyperlinkedModelSerializer):
    def create(self, validated_data):
        return Score.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.player = validated_data.get('player', instance.player)
        instance.hole = validated_data.get('hole', instance.hole)
        instance.total = validated_data.get('total', instance.total)
        instance.save()
        return instance

    class Meta:
        model = Score
        fields = ('id', 'player', 'hole', 'total', 'game')
