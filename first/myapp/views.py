from django.shortcuts import render, HttpResponse
from .models import TodoItem
from .models import NameItem


# Create your views here.

def home(request):
	return render(request, "home.html")

def todos(request):
	items = TodoItem.objects.all()
	return render(request, "todos.html", {"todos": items})

def names(request):
	items = NameItem.objects.all()
	return render(request, "names.html", {"names": items})