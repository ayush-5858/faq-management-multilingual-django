# faq/tests/test_models.py
import pytest
from django.db.utils import IntegrityError
from faq.models import FAQ

@pytest.mark.django_db
def test_faq_creation():
    """Test FAQ creation with English content."""
    faq = FAQ.objects.create(
        question="What is Django?",
        answer="Django is a high-level Python Web framework.",
    )
    assert faq.question == "What is Django?"
    assert faq.answer == "Django is a high-level Python Web framework."

@pytest.mark.django_db
def test_translation_to_hindi():
    """Test automatic translation to Hindi."""
    faq = FAQ.objects.create(
        question="What is Django?",
        answer="Django is a high-level Python Web framework.",
    )
    # Assume the translation happens here, you can check for the translated field
    translated_faq = faq.get_translation('hi')
    assert translated_faq['question']  # Check if translation exists
    assert translated_faq['answer']  # Check if translation exists

@pytest.mark.django_db
def test_translation_to_bengali():
    """Test automatic translation to Bengali."""
    faq = FAQ.objects.create(
        question="What is Django?",
        answer="Django is a high-level Python Web framework.",
    )
    translated_faq = faq.get_translation('bn')
    assert translated_faq['question']  # Check if translation exists
    assert translated_faq['answer']  # Check if translation exists

