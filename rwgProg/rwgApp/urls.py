
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index), # localhost:8000
    path('random_word', views.random), #localhost:8000 + /random_word
]
