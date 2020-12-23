from django import forms

class CommentForm(forms.Form):
    message = forms.CharField(widget=forms.Textarea(attrs={
        'rows': 4,
        'class': 'desktop-comment-box',
        'name': 'message',
        'id': 'message'
    }))
