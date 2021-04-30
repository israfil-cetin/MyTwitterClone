# MyTwitterClone

Virtual Env. Kurulumu Windows
python -m venv venv
venv\Scripts\activate

Paketlerin kurulumu
pip install -r requirements.txt

Kurulum
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser

Django secret-key 
Python terminalinde
from django.core.management.utils import get_random_secret_key  
get_random_secret_key()
Üretilen keyi settings.py dosyasında SECRET_KEY karşısına yazmalı yada ortam değişkeni olarak eklemelisiniz.

Localde Server'ı çalıştırmak
python mangage.py runserver
