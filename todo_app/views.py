from django.shortcuts import render, redirect
from django.views import View
from .forms import InputForm
from .models import TodoModel
import datetime

# Create your views here.
class Main(View):
    def get(self, request):
        data = TodoModel.objects.all().order_by('DeadLine')
        return render(request, "todo_app/main.html", {'data' : data})

class DeleteItem(View):
    def post(self, request, item_id):
        item = TodoModel.objects.get(id=item_id)
        item.delete()
        return redirect('/todo_app/')

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