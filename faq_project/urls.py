from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),  # Admin route
    path('', include('faq.urls')),  # Include routes for the FAQ app
]
