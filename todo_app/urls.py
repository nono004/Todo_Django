from django.urls import path
from .views import Main, Input, Complete, DeleteItem

app_name = 'todoApp'

urlpatterns = [
    path("", Main.as_view(), name='Top'),
    path('delete/<int:item_id>/', DeleteItem.as_view(), name='Delete'),
    path('input/', Input.as_view(), name='Input'),
    path('complete/', Complete.as_view(), name='Complete')
]