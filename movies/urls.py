from django.urls import path
from.views import MoviesCreateListView,MoviesRetrieveUpdateView,MovieStatsView


urlpatterns=[
    path('movies/',MoviesCreateListView.as_view(),name='movies=create-list'),
    path('movies/<int:pk>/',MoviesRetrieveUpdateView.as_view(),name='movies=retrieve-update-delete'),
    path('movies/stats/',MovieStatsView.as_view(),name='movie-stats')
]