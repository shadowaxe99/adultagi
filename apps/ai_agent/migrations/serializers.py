
from rest_framework import serializers
from .models import AIAgent

class AIAgentSerializer(serializers.ModelSerializer):
    class Meta:
        model = AIAgent
        fields = ['id', 'name', 'sample_questions', 'api_key']

    def create(self, validated_data):
        return AIAgent.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.sample_questions = validated_data.get('sample_questions', instance.sample_questions)
        instance.api_key = validated_data.get('api_key', instance.api_key)
        instance.save()
        return instance
