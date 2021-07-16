from django.urls import path
from . import views

urlpatterns = [
    path('', views.index), #localhost:8000/ 
    path('new', views.new), #loclhost:8000/new
    path('create', views.create), #localhost:8000/create
    path('<int:number>', views.number), #localhost:8000/<int>
    path('<int:number>/edit', views.edit), #localhost:8000/<int>/edit
    path('<int:number>/delete', views.destroy), #localhost:8000/<int>/destroy
]