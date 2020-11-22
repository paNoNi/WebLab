from .models import Task
from django.forms import ModelForm, TextInput, Textarea, DateInput, FileInput


class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ['name', 'description', 'date', 'object', 'image']
        widgets = {'name': TextInput(attrs={
            'placeholder': 'Введите название',
            'class': 'form-control',
            'id': "exampleFormControlInput1"
        }),
            'description': Textarea(attrs={
                'placeholder': 'Введите описание',
                'class': 'form-control',
                'id': "exampleFormControlTextarea1",
                'rows': "3"
            }),
            'date': DateInput(attrs={
                'type': "date",
                'class': "form-control"
            }),
            'object': TextInput(attrs={
                'class': "form-control",
                'id': "exampleFormControlInput1",
                'placeholder': "Английский язык"
            }),
            'image': FileInput()
        }
