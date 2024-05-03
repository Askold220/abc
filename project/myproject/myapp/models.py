from django.db import models

class Message(models.Model):
    text = models.TextField()

class Captcha(models.Model):
    image = models.ImageField(upload_to='captcha_images/')
