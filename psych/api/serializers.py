from rest_framework import serializers
from .models import Title, Question, Answer, ok_Answer, profileDetail,Results
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)

    class Meta:
        model = User
        fields = ('id', 'username', 'first_name', 'last_name', 'age', 'password', 'email', 'is_superuser')

class TitleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Title
        fields = '__all__'

class ResultSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)

    class Meta:
        model = Results
        fields = '__all__'

class ResultSerializer2(serializers.ModelSerializer):
    results = ResultSerializer(many=True)
    id = serializers.IntegerField(read_only=True)
    username = serializers.CharField(read_only=True)
    first_name = serializers.CharField(read_only=True)
    last_name = serializers.CharField(read_only=True)
    age = serializers.IntegerField(read_only=True)

    class Meta:
        model = User
        fields = ('id', 'username', 'first_name', 'last_name', 'age', 'results')

class okAnsQuesId(serializers.ModelSerializer):
    id =serializers.IntegerField(read_only=True)

    class Meta:
        model = Question
        fields = ['id']

class OK_AnswerSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)

    class Meta:
        model = ok_Answer
        fields = ('id', 'ok_answer', 'quesId')

class OkAnswerSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    okanswers = OK_AnswerSerializer(many=True)

    class Meta:
        model = Title
        fields = ('id', 'okanswers');

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

