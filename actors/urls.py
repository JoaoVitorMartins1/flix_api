from django.urls import path
from .views import ActorsCreateListView, ActorsRetrieveUpdateDestroyView



urlpatterns=[
    path('actors/',ActorsCreateListView.as_view(),name='actors-create-list'),
    path('actors/<int:pk>/',ActorsRetrieveUpdateDestroyView.as_view(),name='actors-retrieve-update-destroy'),
]