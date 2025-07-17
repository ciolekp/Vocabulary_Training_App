from django.urls import path, include
from . import views
from rest_framework import routers
from .views import WordViewSet

router = routers.DefaultRouter()
router.register(r'api/Word_Trainer', WordViewSet)

urlpatterns = [
    path('learn_english/', views.learn_english, name='learn_english'),
    path('learn_polish/', views.learn_polish, name='learn_polish'),
    path('add_word/', views.add_word, name='add_word'),
    path('register/', views.register, name='register'),
    path("", include(router.urls))
]
