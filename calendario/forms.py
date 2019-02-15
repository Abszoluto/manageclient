from django import forms
from .models import Tarefa

class DateInput(forms.DateInput):
    input_type = 'datetime-local'

class TarefaForm(forms.ModelForm):
    class Meta:
        model = Tarefa
        fields = '__all__'
        widgets = {
            'data_tarefa': DateInput()
        }
