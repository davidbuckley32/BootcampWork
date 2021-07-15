from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index), #localhost8000/
    path('dragons', views.show_dragons), #localhost8000/ + dragons
    path('dragons/create', views.create_dragons), #localhost8000/ + dragons + create
    path('dragons/<int:dragon_id>/edit', views.edit_dragon),
]