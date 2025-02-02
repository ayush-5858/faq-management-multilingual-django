from django.contrib import admin
from .models import FAQ

@admin.register(FAQ)
class FAQAdmin(admin.ModelAdmin):
    # Adjust list_display to show the question and answer fields in all languages
    list_display = ['question', 'answer', 'question_hi', 'answer_hi', 'question_bn', 'answer_bn']
    
    # You can add search functionality for these fields as well
    search_fields = ['question', 'question_hi', 'question_bn']

    # Organize the form in the admin panel
    fieldsets = (
        (None, {
            'fields': ('question', 'answer')  # Main fields in English
        }),
        ('Translations', {
            'fields': ('question_hi', 'answer_hi', 'question_bn', 'answer_bn')  # Translated fields
        }),
    )
