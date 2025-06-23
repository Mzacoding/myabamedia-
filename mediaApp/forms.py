from django import forms

class ContactForm(forms.Form):
    # Field for the user's name
    name = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={'placeholder': 'Your Name'})
    )
    # Field for the user's email address
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={'placeholder': 'Your Email'})
    )
    # Field for the subject of the message
    subject = forms.CharField(
        max_length=200,
        widget=forms.TextInput(attrs={'placeholder': 'Subject'})
    )
    # Field for the main message content
    message = forms.CharField(
        widget=forms.Textarea(attrs={'placeholder': 'Your Message', 'rows': 5})
    )
