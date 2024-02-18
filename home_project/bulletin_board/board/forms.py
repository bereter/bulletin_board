from django import forms
from .models import Post, Comment


class CreateFormBoard(forms.ModelForm):
    class Meta:
        model = Post
        fields = [
            'name',
            'text',
            'category'
        ]


class CreateFormComment(forms.ModelForm):
    class Meta:
        model = Comment
        fields = [
            'text',
        ]

