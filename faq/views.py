from django.http import JsonResponse, HttpResponse
from .models import FAQ

def home(request):
    return HttpResponse("Welcome to the FAQ App!")

def get_faqs(request):
    lang = request.GET.get('lang', 'en')  # Default to English if no language is specified
    faqs = FAQ.objects.all()
    data = [
        {
            "question": faq.get_translation(lang)['question'],
            "answer": faq.get_translation(lang)['answer']
        }
        for faq in faqs
    ]
    return JsonResponse(data, safe=False)
