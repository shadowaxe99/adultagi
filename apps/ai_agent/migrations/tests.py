
import pytest
from django.urls import reverse
from rest_framework.test import APIClient
from apps.ai_agent.models import AIAgent

@pytest.fixture
def api_client():
    return APIClient()

@pytest.fixture
def create_ai_agent():
    AIAgent.objects.create(name="Test Agent", api_key="1234567890")

def test_ai_agent_creation(api_client, create_ai_agent):
    response = api_client.get(reverse('ai_agent_list'))
    assert response.status_code == 200
    assert len(response.data) == 1

def test_ai_agent_detail(api_client, create_ai_agent):
    response = api_client.get(reverse('ai_agent_detail', kwargs={'pk': create_ai_agent.pk}))
    assert response.status_code == 200
    assert response.data['name'] == 'Test Agent'
    assert response.data['api_key'] == '1234567890'
