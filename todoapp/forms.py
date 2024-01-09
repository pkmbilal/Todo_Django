from django import forms
from .models import Todo

class CreateTodo(forms.ModelForm):
    class Meta:
        model = Todo
        fields = '__all__'
        widgets = {
            'todoName': forms.TextInput(attrs={'placeholder': 'Enter todo name', 'class': 'block w-full p-4 text-lg outline-none border-2 border-gray-100', 'autofocus':'True'})
        }