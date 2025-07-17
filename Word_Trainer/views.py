from django.shortcuts import render, redirect
from .models import Word
from .forms import WordForm
from .serializers import WordSerializer
import random
from rest_framework import viewsets
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login as auth_login
from django.contrib.auth.decorators import login_required

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('learn_english')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})

@login_required
def learn_english(request):
    words = list(Word.objects.all())
    if words:
        word = random.choice(words)
    else:
        word = None
    return render(request, 'learn_english.html', {'word': word})

@login_required
def learn_polish(request):
    words = list(Word.objects.all())
    if words:
        word = random.choice(words)
    else:
        word = None
    return render(request, 'learn_polish.html', {'word': word})

@login_required
def add_word(request):
    if request.method == 'POST':
        form = WordForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('learn_english')
    else:
        form = WordForm()
    return render(request, 'add_word.html', {'form':form})

class WordViewSet(viewsets.ModelViewSet):
    queryset = Word.objects.all()
    serializer_class = WordSerializer
