from django.shortcuts import render
from django.http import HttpResponse

class Finch:
  def __init__(self, name, type, description, age):
    self.name = name
    self.type = type
    self.description = description
    self.age = age

finches = [
  Finch('Gary', 'spice finch', 'not afraid to make things spicy', 6),
  Finch('Chirp', 'society finch', 'always chirping at folks', 2),
  Finch('Nelly', 'strawberry finch', 'looks the best', 0),
  Finch('Chris', 'blue finch', 'head coach of the timberwolves', 3),
]


# Create your views here.

def home(request):
    return HttpResponse('<h1>Master Finch Collector</h1>')

def about(request):
    return render(request, 'about.html')

def finches_index(request):
    return render(request, 'finches/index.html', { 'finches': finches })