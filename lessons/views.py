from rest_framework import viewsets, generics
from .models import Lesson, Subject
from django.contrib.auth import get_user_model
from .serializers import LessonSerializer, SubjectSerializer, UserSerializer

User = get_user_model()

class LessonViewSet(viewsets.ModelViewSet):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    
class LessonListBySubject(generics.ListAPIView):
    serializer_class = LessonSerializer

    def get_queryset(self):
        subject_id = self.kwargs['subject_id']
        return Lesson.objects.filter(subject_id=subject_id)

class SubjectListView(generics.ListAPIView):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer
    
    
class UserListAPIView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer