from django import forms
from .models import Post

class CommentForm(forms.Form):
    message = forms.CharField(widget=forms.Textarea(attrs={
        'rows': 4,
        'class': 'desktop-comment-box',
        'name': 'message',
        'id': 'message'
    }))


class PostForm(forms.Form):
    caption = forms.CharField(widget=forms.Textarea(attrs={
        'rows': 4,
        'class': 'desktop-comment-box',
        'name': 'message',
        'id': 'message'
    }))

    image = forms.ImageField()