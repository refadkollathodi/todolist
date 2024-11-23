from django import forms 
from todo.models import todo
# from django.forms import TextInput

class TodoForm(forms.ModelForm):
    class Meta:
        model = todo
        fields = '__all__'
        widgets = {
            'task': forms.Textarea(attrs={
                'class': 'no-arrows',
                'placeholder':'enter your task',
            }),
        }