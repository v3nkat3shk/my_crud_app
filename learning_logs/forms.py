from django import forms
from django.forms import widgets
from .models import Entry, Topic


class TopicForm(forms.ModelForm):
    class Meta:
        model = Topic
        fields = ['text']
        labels = {'text': ''}


class EntryForm(forms.ModelForm):
    class Meta:
        model = Entry
        fields = ['text']
        lablels = {'text': 'Entry:'}
        widgets = {'text': forms.Textarea(attrs={'cols': 100})}
