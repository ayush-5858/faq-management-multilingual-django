from django.db import models
from ckeditor.fields import RichTextField
from googletrans import Translator  # Import Google Translate API

class FAQ(models.Model):
    # Main fields in English
    question = models.TextField()  # Main question in English
    answer = RichTextField()  # WYSIWYG support for the answer

    # Translation fields for other languages
    question_hi = models.TextField(blank=True, null=True, verbose_name="Hindi Question")
    question_bn = models.TextField(blank=True, null=True, verbose_name="Bengali Question")

    answer_hi = RichTextField(blank=True, null=True, verbose_name="Hindi Answer")
    answer_bn = RichTextField(blank=True, null=True, verbose_name="Bengali Answer")

    def get_translation(self, lang='en'):
        """Return the translated question and answer based on the language code.
        Automatically translate if translation is missing."""
        
        translator = Translator()  # Initialize the translator

        if lang == 'hi':
            # Translate if Hindi translation doesn't exist
            if not self.question_hi:
                self.question_hi = translator.translate(self.question, src='en', dest='hi').text
            if not self.answer_hi:
                self.answer_hi = translator.translate(self.answer, src='en', dest='hi').text
            return {
                'question': self.question_hi,
                'answer': self.answer_hi
            }
        elif lang == 'bn':
            # Translate if Bengali translation doesn't exist
            if not self.question_bn:
                self.question_bn = translator.translate(self.question, src='en', dest='bn').text
            if not self.answer_bn:
                self.answer_bn = translator.translate(self.answer, src='en', dest='bn').text
            return {
                'question': self.question_bn,
                'answer': self.answer_bn
            }
        return {
            'question': self.question,
            'answer': self.answer
        }

    def __str__(self):
        return self.question
