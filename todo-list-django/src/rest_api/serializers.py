from rest_framework import serializers
from .models import ToDo


class ToDoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ToDo
        # fields = ('id', 'todo', 'started_on', 'due_on', 'description')
        fields = '__all__'
