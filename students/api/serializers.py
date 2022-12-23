from rest_framework import serializers
from students.models import Students


class StudentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Students
        fields = ('id', 'first_name', 'last_name', 'date_of_birth',
                  'grade', 'phone', 'email', 'created_at')
        read_only_fields = ('created_at',)
