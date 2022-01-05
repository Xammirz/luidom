import os
import sys
from datetime import datetime

proj = os.path.dirname(os.path.abspath('manage.py'))

sys.path.append(proj)

os.environ['DJANGO_SETTINGS_MODULE'] = 'core.settings'

import django
django.setup()

from django.core.mail import EmailMultiAlternatives
from core.settings import EMAIL_HOST_USER
from index.models import Follower

emails = Follower.objects.all()
subject = 'ТЕСТ'
from_email = EMAIL_HOST_USER
text_content = 'Тест !'
html_content = ''
for email in emails: 
    
  html_content += f'''<h1>ВСЕМ ПриВеТ</h1>'''
  msg = EmailMultiAlternatives(subject, text_content, from_email, [email])
  msg.attach_alternative(html_content, "text/html")
  msg.send()