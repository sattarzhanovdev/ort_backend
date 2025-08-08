from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import LessonViewSet, LessonListBySubject, SubjectListView, UserListAPIView
from rest_framework.authtoken.views import obtain_auth_token

router = DefaultRouter()
router.register(r'lessons', LessonViewSet)

urlpatterns = [
  path('', include(router.urls)),
  path('lessons/subject/<int:subject_id>/', LessonListBySubject.as_view()),
  path('subjects/', SubjectListView.as_view()),
  path('users/', UserListAPIView.as_view()),
  path('login/', obtain_auth_token),
]