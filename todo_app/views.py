from django.shortcuts import render, redirect
from django.views import View
from .forms import InputForm

# Create your views here.
class Main(View):
    def get(self, request):
        return render(request, "todo_app/main.html")

class Input(View):
    def get(self, request):
        form = InputForm()
        return render(request, "todo_app/input.html", {'form':form})

    def post(self, request):
        form = InputForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/todo_app/complete/')
        else:
            form = InputForm()
        return render(request, 'todo_app/input.html', {'form':form})

class Complete(View):
    def get(self, request):
        return render(request, "todo_app/complete.html")