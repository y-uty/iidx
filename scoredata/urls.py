from django.urls import path
from . import views

urlpatterns = [
    path('score/entry/', views.score_entry, name='score_entry'),
    path('score/entry/exec', views.score_entry_exec, name='score_entry_exec'),
    path('score/view/', views.score_view, name='score_view'),
]