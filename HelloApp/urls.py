from django.urls import path
from .views import HelloApp

urlpatterns = [
    path('', HelloApp.as_view()),
]