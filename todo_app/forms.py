from django import forms
from .models import TodoModel

class InputForm(forms.ModelForm):
    #ToDo = forms.CharField(widget=forms.Textarea(attrs={'class':'textarea', 'placeholder':'ToDoを入力'}))
    #DeadLine = forms.DateField(widget=forms.DateInput(attrs={'type':'date', 'class':'date'}))
    class Meta:
        model = TodoModel
        fields = ['Todo', 'DeadLine', 'Category']
        widgets = {
            'Todo': forms.Textarea(attrs={'class': 'textarea', 'placeholder': 'ToDoを入力'}),
            'DeadLine': forms.DateInput(attrs={'type': 'date', 'class': 'date'}),
            'Category' : forms.Select(attrs={'class': 'Category'})
        }
        labels = {
            'Todo': 'ToDo',  # ToDoフィールドのラベルを変更
            'DeadLine': '期限',  # DeadLineフィールドのラベルを変更
            'Category': 'カテゴリ',  # Categoryフィールドのラベルを変更
        }