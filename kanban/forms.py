from django import forms
from .models.kanban import Issue

class IssueForm(forms.ModelForm):
    class Meta:
        model = Issue
        fields = ['title', 'description']
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline',
                'placeholder': 'Enter issue title',
                'id': 'id_title'
            }),
            'description': forms.Textarea(attrs={
                'class': 'shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline',
                'placeholder': 'Enter issue description',
                'id': 'id_description'
            }),
        }

class CommentForm(forms.Form):
    issue = forms.ModelChoiceField(queryset=Issue.objects.all())
    comment = forms.CharField(widget=forms.Textarea)
