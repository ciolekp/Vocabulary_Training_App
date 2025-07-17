# from django.contrib import admin
from django.urls import path
from . import views
from rest_framework import routers
from .views import WordViewSet

urlpatterns = [
    path('learn_english/', views.learn_english, name='learn_english'),
    path('learn_polish/', views.learn_polish, name='learn_polish'),
    path('add_word/', views.add_word, name='add_word'),
    path('register/', views.register, name='register'),
]

router = routers.DefaultRouter()
router.register(r'api/Word_Trainer', WordViewSet)

urlpatterns += router.urls


