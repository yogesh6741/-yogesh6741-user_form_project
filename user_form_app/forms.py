from django import forms
from .models import UserForm

class UserFormForm(forms.ModelForm):
    class Meta:
        model = UserForm
        fields = ('name', 'date_of_birth', 'email', 'phone_number')
