from .models import Comment, Post, Contact
from django import forms

class CommentForm(forms.ModelForm):
    """ Form for posting comments """
    class Meta:
        model = Comment
        fields = ('body',)
        widgets = {
            'body': forms.Textarea(attrs={'cols': 40, 'rows': 3}),
        }


class ContactForm(forms.ModelForm):
    """"Form for contact us page"""
    class Meta:
        model = Contact
        fields = ('first_name', 'last_name', 'email', 'body',)


class PostAddForm(forms.ModelForm):
    """ Form for adding or editing posts """
    class Meta:
        model = Post
        fields = ('category', 'title', 'body', 'image', 'id',)


class PostEditForm(forms.ModelForm):
    """ Form for adding or editing posts """
    class Meta:
        model = Post
        fields = ('category', 'title', 'body', 'id',)

