from django import forms
from .models import Feedback

class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ['topic', 'name', 'email', 'message']  # Include only the relevant fields
        widgets = {
            'topic': forms.Select(attrs={
                'class': 'form-control',
                'placeholder': 'Select Feedback Topic',
            }),
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter your name (optional)',
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter your email (optional)',
            }),
            'message': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Write your feedback here...',
                'rows': 6,
            }),
        }
        labels = {
            'topic': 'Feedback Topic',
            'name': 'Your Name (optional)',
            'email': 'Your Email (optional)',
            'message': 'Your Feedback',
        }
