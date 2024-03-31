from .models import MyModel
from django.forms import ModelForm, TextInput, Textarea


class MainForm(ModelForm):
    class Meta:
        model = MyModel
        fields = ['name', 'description']

        widgets = {
            'name': TextInput(attrs={'class': 'form-control', 'placeholder': 'Имя'}),
            'description': Textarea(attrs={'class': 'form-control', 'placeholder': 'Описание'}),
        }