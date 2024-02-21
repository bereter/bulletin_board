from django_filters import FilterSet, DateTimeFilter
from .models import Post
from django import forms


class PostFilter(FilterSet):
    date = DateTimeFilter(
        widget=forms.DateInput(attrs={'type': 'date'}),
        lookup_expr='date__lte'
    )

    class Meta:
        model = Post
        fields = {
            'category': ['exact'],
        }


class PostFilterUser(FilterSet):
    date = DateTimeFilter(
        widget=forms.DateInput(attrs={'type': 'date'}),
        lookup_expr='date__lte'
    )