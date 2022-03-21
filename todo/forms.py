from statistics import mode
from django.forms import ModelForm

from .forms import TodoForm
from .models import Todo

class TodoForm(ModelForm):
    class Meta:
        model = Todo
        fields = ['title', 'description', 'is_done']