# counter/urls.py
from django.urls import path
from .views import get_counter, increment_counter, decrement_counter,reset_counter

urlpatterns = [
    path('get-counter/', get_counter, name='get_counter'),
    path('increment-counter/', increment_counter, name='increment_counter'),
    path('decrement-counter/', decrement_counter, name='decrement_counter'),
    path('reset-counter/', reset_counter, {'action': 'reset'}, name='reset_counter'),
]
