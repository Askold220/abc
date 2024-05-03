from django.contrib import admin
from .models import Message, Captcha

admin.site.register(Message)
admin.site.register(Captcha)
