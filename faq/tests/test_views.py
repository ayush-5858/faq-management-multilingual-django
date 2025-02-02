# faq/tests/test_views.py
import pytest
from django.urls import reverse
from rest_framework import status
from faq.models import FAQ

@pytest.mark.django_db
def test_get_faqs_english(client):
    """Test fetching FAQs in English."""
    faq = FAQ.objects.create(
        question="What is Django?",
        answer="Django is a high-level Python Web framework.",
    )
    url = reverse('get_faqs') + '?lang=en'
    response = client.get(url)  # 'client' is a test client provided by pytest-django
    assert response.status_code == status.HTTP_200_OK
    data = response.json()
    assert len(data) == 1  # We expect one FAQ
    assert data[0]['question'] == faq.question
    assert data[0]['answer'] == faq.answer

@pytest.mark.django_db
def test_get_faqs_hindi(client):
    """Test fetching FAQs in Hindi."""
    faq = FAQ.objects.create(
        question="What is Django?",
        answer="Django is a high-level Python Web framework.",
    )
    url = reverse('get_faqs') + '?lang=hi'
    response = client.get(url)
    assert response.status_code == status.HTTP_200_OK
    data = response.json()
    assert len(data) == 1
    assert data[0]['question'] != faq.question  # Translated question
    assert data[0]['answer'] != faq.answer  # Translated answer

@pytest.mark.django_db
def test_get_faqs_bengali(client):
    """Test fetching FAQs in Bengali."""
    faq = FAQ.objects.create(
        question="What is Django?",
        answer="Django is a high-level Python Web framework.",
    )
    url = reverse('get_faqs') + '?lang=bn'
    response = client.get(url)
    assert response.status_code == status.HTTP_200_OK
    data = response.json()
    assert len(data) == 1
    assert data[0]['question'] != faq.question  # Translated question
    assert data[0]['answer'] != faq.answer  # Translated answer
