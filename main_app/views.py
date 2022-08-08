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
    return HttpResponse('<img src="https://media.istockphoto.com/vectors/set-of-colorful-birds-isolated-on-white-background-vector-id1155378512?k=20&m=1155378512&s=612x612&w=0&h=8mKT5zEt0XtyvjLss0UkpVM3buJqsPH2aKJKZwD3n3Y=">')

def about(request):
    return render(request, 'about.html')

def finches_index(request):
    return render(request, 'finches/index.html', { 'finches': finches })