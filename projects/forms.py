from django import forms
from .models import Project
from django.contrib.auth.models import User

class ProjectForm(forms.ModelForm):
    name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'id': "project-name",
                'aria - describedby': "input-helper-text",
                'class': 'form-input',
                'placeholder': "Project Name",
            }))
    description = forms.CharField(
        widget=forms.Textarea(
                attrs={
                    'rows': 8,
                    'class': "form-input",
                    'id': "project-description",
                    'placeholder': "Project Description",
                }))
    status = forms.ChoiceField(
        widget=forms.RadioSelect(
            attrs={
                'class': 'form-radio',
                'id': 'team',
                   }
        ),
        choices=[('Private', 'Private'), ('Public', 'Public'), ('Team', 'Team')],
    )
    price = forms.IntegerField(
        widget=forms.NumberInput(
            attrs={
                'class': 'form-input',
                'id': "budget",
                'placeholder': "Budget of the project",
            }
        )
    )
    users = forms.ModelMultipleChoiceField(
        queryset=User.objects.all(),  # Assuming you want to select from all Users
        widget=forms.SelectMultiple(attrs={
            'class': "form-input",
            }
        )
    )
    due_date = forms.DateField(
        widget=forms.DateInput(attrs={
            'class': 'form-input',
            'id': "budget-date",
        }
        )
    )


    class Meta:
        model = Project
        fields = ('name', 'description', 'category', 'price', 'progress', 'status', 'users','image', 'due_date')
