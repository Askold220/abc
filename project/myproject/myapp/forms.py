from django import forms
from captcha.fields import CaptchaField

class MessageForm(forms.Form):
    text = forms.CharField(widget=forms.Textarea)
    captcha = CaptchaField()
