from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # Home route for FAQ app
    path('faqs/', views.get_faqs, name='get_faqs'),  # API route to get FAQs by language
]
