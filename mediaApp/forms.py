from django import forms
from django.core.validators import RegexValidator
import re


class ContactForm(forms.Form):
    """Professional contact form with enhanced validation and security."""
    
    # Name field with enhanced validation
    name = forms.CharField(
        max_length=100,
        min_length=2,
        widget=forms.TextInput(attrs={
            'placeholder': 'Your Full Name',
            'class': 'form-control',
            'required': True,
            'autocomplete': 'name'
        }),
        validators=[
            RegexValidator(
                regex=r'^[a-zA-Z\s\-\']+$',
                message='Name can only contain letters, spaces, hyphens, and apostrophes.'
            )
        ],
        help_text='Enter your full name (2-100 characters)'
    )
    
    # Email field with enhanced validation
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={
            'placeholder': 'your.email@example.com',
            'class': 'form-control',
            'required': True,
            'autocomplete': 'email'
        }),
        help_text='We\'ll never share your email with anyone else.'
    )
    
    # Subject field with enhanced validation
    subject = forms.CharField(
        max_length=200,
        min_length=5,
        widget=forms.TextInput(attrs={
            'placeholder': 'Brief description of your inquiry',
            'class': 'form-control',
            'required': True
        }),
        help_text='Briefly describe what your message is about (5-200 characters)'
    )
    
    # Message field with enhanced validation
    message = forms.CharField(
        min_length=10,
        max_length=2000,
        widget=forms.Textarea(attrs={
            'placeholder': 'Please provide details about your inquiry, project requirements, or how we can help you...',
            'class': 'form-control',
            'rows': 6,
            'required': True
        }),
        help_text='Provide detailed information about your inquiry (10-2000 characters)'
    )
    
    def clean_name(self):
        """Custom validation for name field."""
        name = self.cleaned_data.get('name')
        if name:
            # Remove extra whitespace
            name = ' '.join(name.split())
            # Check for minimum word count
            if len(name.split()) < 1:
                raise forms.ValidationError('Please enter at least your first name.')
        return name
    
    def clean_email(self):
        """Custom validation for email field."""
        email = self.cleaned_data.get('email')
        if email:
            # Convert to lowercase
            email = email.lower().strip()
            # Additional email validation
            if not re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', email):
                raise forms.ValidationError('Please enter a valid email address.')
        return email
    
    def clean_subject(self):
        """Custom validation for subject field."""
        subject = self.cleaned_data.get('subject')
        if subject:
            # Remove extra whitespace
            subject = ' '.join(subject.split())
            # Check for spam-like content
            spam_keywords = ['free', 'urgent', 'act now', 'limited time']
            if any(keyword in subject.lower() for keyword in spam_keywords):
                raise forms.ValidationError('Subject contains suspicious content.')
        return subject
    
    def clean_message(self):
        """Custom validation for message field."""
        message = self.cleaned_data.get('message')
        if message:
            # Remove extra whitespace but preserve line breaks
            message = '\n'.join(' '.join(line.split()) for line in message.split('\n'))
            # Check for minimum word count
            word_count = len(message.split())
            if word_count < 5:
                raise forms.ValidationError('Please provide a more detailed message (at least 5 words).')
        return message
    
    def clean(self):
        """Overall form validation."""
        cleaned_data = super().clean()
        name = cleaned_data.get('name')
        email = cleaned_data.get('email')
        subject = cleaned_data.get('subject')
        message = cleaned_data.get('message')
        
        # Check if name appears to be in email format (common mistake)
        if name and '@' in name:
            raise forms.ValidationError('Please enter your name in the name field, not your email address.')
        
        # Ensure message is not just repetition of subject
        if subject and message and subject.lower() == message.lower():
            raise forms.ValidationError('Please provide additional details in the message field.')
        
        return cleaned_data