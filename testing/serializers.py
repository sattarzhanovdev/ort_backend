from rest_framework import serializers
from .models import Test, TestPage, Answer

class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = ["question_number", "correct_option"]  # теперь отдаем и правильный ответ

class TestPagePublicSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(use_url=True)
    answers = AnswerSerializer(many=True, read_only=True)  # сюда попадут правильные ответы

    class Meta:
        model = TestPage
        fields = ["id", "page_number", "image", "answers"]

class TestListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Test
        fields = ["id", "title", "is_trial", "created_at"]

class TestDetailPublicSerializer(serializers.ModelSerializer):
    pages = TestPagePublicSerializer(many=True, read_only=True)

    class Meta:
        model = Test
        fields = ["id", "title", "is_trial", "created_at", "pages"]