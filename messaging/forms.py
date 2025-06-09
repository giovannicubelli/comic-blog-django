from django import forms
from .models import Message
from django.contrib.auth.models import User

class MessageForm(forms.ModelForm):
    # Permitir seleccionar destinatario, pero no el remitente (se asigna automáticamente)
    recipient = forms.ModelChoiceField(
        queryset=User.objects.all(), # Podrías filtrar para no enviarse a uno mismo o admin
        widget=forms.Select(attrs={'class': 'form-control'}),
        label="Destinatario"
    )
    class Meta:
        model = Message
        fields = ['recipient', 'subject', 'body']
        widgets = {
            'subject': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Asunto (opcional)'}),
            'body': forms.Textarea(attrs={'class': 'form-control', 'rows': 5, 'placeholder': 'Escribe tu mensaje...'}),
        }
        labels = {
            'body': 'Mensaje'
        }