from django import forms
from main.models import Send

class Sendd(forms.ModelForm):
    class Meta:
        model = Send
        fields = ("full", "email", "subject", "message")