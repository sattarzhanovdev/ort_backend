from django.contrib import admin
from .models import Test, TestPage, Answer


class AnswerInline(admin.TabularInline):
    model = Answer
    extra = 0
    fields = ("question_number", "correct_option")
    ordering = ("question_number",)


@admin.register(Test)
class TestAdmin(admin.ModelAdmin):
    list_display = ("title", "is_trial", "created_at")
    list_filter = ("is_trial",)
    search_fields = ("title",)


@admin.register(TestPage)
class TestPageAdmin(admin.ModelAdmin):
    list_display = ("__str__", "test", "page_number")
    list_filter = ("test",)
    inlines = [AnswerInline]