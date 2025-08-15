from django.db import models

OPTION_LABELS = (
    ('A', 'А'),
    ('B', 'Б'),
    ('C', 'В'),
    ('D', 'Г'),
)

class Test(models.Model):
    title = models.CharField(max_length=255, verbose_name="Название теста")
    is_trial = models.BooleanField(default=False, verbose_name="Пробный тест")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Тест"
        verbose_name_plural = "Тесты"
        ordering = ["-created_at"]

    def __str__(self):
        return self.title


class TestPage(models.Model):
    test = models.ForeignKey(Test, on_delete=models.CASCADE, related_name="pages", verbose_name="Тест")
    image = models.ImageField(upload_to="tests/pages/", verbose_name="Изображение страницы")
    page_number = models.PositiveIntegerField(default=1, verbose_name="Номер страницы")

    class Meta:
        verbose_name = "Страница теста"
        verbose_name_plural = "Страницы теста"
        ordering = ["test", "page_number"]

    def __str__(self):
        return f"{self.test} — стр. {self.page_number}"


class Answer(models.Model):
    page = models.ForeignKey(TestPage, on_delete=models.CASCADE, related_name="answers", verbose_name="Страница теста")
    question_number = models.PositiveIntegerField(verbose_name="Номер вопроса")
    correct_option = models.CharField(max_length=1, choices=OPTION_LABELS, verbose_name="Правильный вариант")

    class Meta:
        verbose_name = "Ответ"
        verbose_name_plural = "Ответы"
        ordering = ["question_number"]
        unique_together = ("page", "question_number")

    def __str__(self):
        return f"Вопрос {self.question_number}: {self.correct_option}"