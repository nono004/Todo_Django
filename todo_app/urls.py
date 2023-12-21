from django.urls import path
from .views import Main, Input, Complete

app_name = 'todo_app'

urlpatterns = [
    path("", Main.as_view(), name='Top'),
    path('input/', Input.as_view(), name='Input'),
    path('complete/', Complete.as_view(), name='Complete')
]