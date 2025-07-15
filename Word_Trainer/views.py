from django.shortcuts import render, redirect
# from django.contrib.auth.decorators import login_required
from .models import Word
from .forms import WordForm
import random
from rest_framework import viewsets
from .serializers import WordSerializer


class WordViewSet(viewsets.ModelViewSet):
    queryset = Word.objects.all()
    serializer_class = WordSerializer

def learn_english(request):
    words = list(Word.objects.all())
    if words:
        word = random.choice(words)
    else:
        word = None
    return render(request, 'learn_english.html', {'word': word})

def learn_polish(request):
    words = list(Word.objects.all())
    if words:
        word = random.choice(words)
    else:
        word = None
    return render(request, 'learn_polish.html', {'word': word})

def add_word(request):
    if request.method == 'POST':
        form = WordForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('learn_english')
    else:
        form = WordForm()
    return render(request, 'add_word.html', {'form':form})

