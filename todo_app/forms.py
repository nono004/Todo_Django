from django import forms
from .models import TodoModel

class InputForm(forms.ModelForm):
    #ToDo = forms.CharField(widget=forms.Textarea(attrs={'class':'textarea', 'placeholder':'ToDoを入力'}))
    #DeadLine = forms.DateField(widget=forms.DateInput(attrs={'type':'date', 'class':'date'}))
    class Meta:
        model = TodoModel
        fields = ['Todo', 'DeadLine', 'Category']