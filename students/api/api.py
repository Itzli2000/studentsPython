from rest_framework import viewsets, permissions
from ..models import Students
from .serializers import StudentsSerializer


class StudentsViewSet(viewsets.ModelViewSet):
    queryset = Students.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = StudentsSerializer