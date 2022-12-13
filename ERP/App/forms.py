from django import forms

from .models import Apps

class AppForms(forms.ModelForm):

    class Meta:

        model = Apps

        fields = ('user_name', 'user_email')
