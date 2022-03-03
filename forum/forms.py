from .models import Comment, Post, Contact
from django import forms


class CommentForm(forms.ModelForm):
    """ Form for posting comments """
    class Meta:
        model = Comment
        fields = ('body', 'image',)
        widgets = {
            'body': forms.Textarea(attrs={'cols': 40, 'rows': 3}),
        }


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ('first_name', 'last_name', 'email', 'body',)
