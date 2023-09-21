
from django.contrib import admin
from .models import AIAgent

@admin.register(AIAgent)
class AIAgentAdmin(admin.ModelAdmin):
    list_display = ('name', 'api_key', 'sample_questions')
    search_fields = ('name',)
