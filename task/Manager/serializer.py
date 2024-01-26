from rest_framework import serializers
from .models import Tasks
from django.contrib.auth.models import User


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tasks
        fields = ['id', 'title', 'description', 'due_date', 'status', 'owner']
    # owner = serializers.ReadOnlyField(source='owner.username')

    def create(self, validated_data):

        return Tasks.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.description = validated_data.get('description', instance.description)
        instance.due_date = validated_data.get('due_date', instance.due_date)
        instance.status = validated_data.get('status', instance.status)
        instance.save()
        return instance    

class UserSerializer(serializers.ModelSerializer):
    tasks = serializers.PrimaryKeyRelatedField(many=True, queryset=Tasks.objects.all())

    class Meta:
        model = User
        fields = ['id', 'username', 'tasks']
