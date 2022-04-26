from django.urls import path
from . import views

urlpatterns = [
    path('Song/', views.song_list),
]