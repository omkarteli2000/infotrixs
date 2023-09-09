from django import forms
from .models import Messages

class message_gen_form(forms.ModelForm):
    class Meta:
        model = Messages
        fields = ['message']