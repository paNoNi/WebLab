from .models import Task, UserTasks
from django.forms import ModelForm, TextInput, Textarea, DateInput, FileInput


class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ['name', 'description', 'date', 'object', 'image']
        widgets = {'name': TextInput(attrs={
            'placeholder': 'Введите названи'
        }),
            'description': Textarea(attrs={
                'placeholder': 'Введите описание'
            }),
            'date': DateInput(),
            'object': TextInput(),
            'image': FileInput()}
