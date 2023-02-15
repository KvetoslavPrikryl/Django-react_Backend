from django.urls import path
from . import views

urlpatterns = [
    path("", views.getRoutes , name="routes"),
    path("notes/", views.getNotes, name="noutes"),
    path("notes/<str:pk>", views.getNote, name="noute"),
    path("notes/<str:pk>/update", views.updateNote, name="update-note")
]
