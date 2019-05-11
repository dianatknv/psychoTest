from rest_framework import serializers
from .models import Title, Question, Answer, ok_Answer, profileDetail
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email')

class TitleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Title
        fields = '__all__'

class ProfileDetailSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    class Meta:
        model = profileDetail
        fields = '__all__'

class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = ('id', 'answer')

class QuestionSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    answers = AnswerSerializer(many=True)

    class Meta:
        model = Question
        fields = ('id', 'question', 'answers')

class TitleSerializer2(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(required=True)
    questions = QuestionSerializer(many=True)

    class Meta:
        model = Title
        fields = ('id', 'name', 'questions')

    def create(self, validated_data):
        questions = validated_data.pop('questions')
        title = Title.objects.create(**validated_data)
        arr = [Question(title=title, **q) for q in questions]
        Question.objects.bulk_create(arr)
        return title

class Ok_AnswerSerializer(serializers.Serializer):
    id = serializers.IntegerField(required=True)
    question = serializers.IntegerField(read_only=True)
    ok_answer = serializers.CharField(required=True)
