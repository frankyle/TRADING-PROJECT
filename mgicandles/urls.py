# urls.py
from django.urls import path
from .views import MgiCandlesListView, MgiCandlesDetailView

urlpatterns = [
    path('mgicandles/', MgiCandlesListView.as_view(), name='mgicandles-list'),
    path('mgicandles/<int:pk>/', MgiCandlesDetailView.as_view(), name='mgicandles-detail'),
]
