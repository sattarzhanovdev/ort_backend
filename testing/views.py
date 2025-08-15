from rest_framework import viewsets, mixins
from rest_framework.permissions import AllowAny, IsAdminUser
from django.db.models import Prefetch
from .models import Test, TestPage, Answer
from .serializers import TestListSerializer, TestDetailPublicSerializer

class TestViewSet(mixins.ListModelMixin,
                  mixins.RetrieveModelMixin,
                  viewsets.GenericViewSet):

    def get_permissions(self):
        if self.action == "retrieve" and self.request.query_params.get("with_answers") == "true":
            return [IsAdminUser()]  # правильные ответы только для админа
        return [AllowAny()]

    def get_queryset(self):
        qs = Test.objects.all().prefetch_related(
            Prefetch(
                "pages",
                queryset=TestPage.objects.order_by("page_number").prefetch_related(
                    Prefetch("answers", queryset=Answer.objects.order_by("question_number"))
                ),
            )
        )
        return qs

    def get_serializer_class(self):
        if self.action == "list":
            return TestListSerializer
        return TestDetailPublicSerializer