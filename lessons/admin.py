from django.contrib import admin
from .models import Lesson, LessonImage, Question, Answer, Subject

class AnswerInline(admin.TabularInline):
    model = Answer
    extra = 1  # сколько пустых строк по умолчанию
    fields = ['text', 'is_correct']
    show_change_link = False

class QuestionAdmin(admin.ModelAdmin):
    inlines = [AnswerInline]

class LessonImageInline(admin.TabularInline):
    model = LessonImage
    extra = 1

class LessonAdmin(admin.ModelAdmin):
    inlines = [LessonImageInline]
    

admin.site.register(Lesson, LessonAdmin)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Subject)
