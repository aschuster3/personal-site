from core.models import Message

from django import forms

class MessageForm(forms.ModelForm):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    message = forms.TextInput()

    class Meta:
        model = Message
        fields = {'name', 'email', 'message'}
