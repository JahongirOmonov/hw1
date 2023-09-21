from django.urls import path
from .views import CreateAPIView, ListAPIView, UpdateStatus



urlpatterns=[
    path('CreateAPIView/', CreateAPIView.as_view()),
    path('ListAPIView/', ListAPIView.as_view()),
    path('UpdateStatus/<int:forid>', UpdateStatus.as_view()),
]