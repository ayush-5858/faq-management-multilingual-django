# faq-management-multilingual-django
# FAQ App

A Django-based FAQ management system that supports multi-language translations (English, Hindi, Bengali) using the Google Translate API. The project features a WYSIWYG editor for FAQ answers, automatic translation of questions, caching for improved performance with Redis, and a REST API for fetching FAQs in different languages.

## Features:
- Multi-language support (English, Hindi, Bengali).
- WYSIWYG editor for FAQ answers (using `django-ckeditor`).
- Automatic translation of questions during object creation using Google Translate API.
- Caching of translations for improved performance.
- REST API for fetching FAQs in different languages.
- User-friendly Django Admin interface for managing FAQs.
- 
## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/faq-app.git
   cd faq-app
   ```

2. Install the dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Set up the database:
   ```bash
   python manage.py migrate
   ```

4. Create a superuser for the admin panel:
   ```bash
   python manage.py createsuperuser
   ```

5. Run the application:
   ```bash
   python manage.py runserver
   ```

## API Usage

- Fetch FAQs in English:
  ```bash
  curl http://localhost:8000/api/faqs/
  ```

- Fetch FAQs in Hindi:
  ```bash
  curl http://localhost:8000/api/faqs/?lang=hi
  ```

- Fetch FAQs in Bengali:
  ```bash
  curl http://localhost:8000/api/faqs/?lang=bn
  ```

## Docker Support

To run the app with Docker:

1. Build the Docker images:
   ```bash
   docker-compose build
   ```

2. Run the containers:
   ```bash
   docker-compose up
   ```

## Tests

To run the tests:
```bash
pytest
