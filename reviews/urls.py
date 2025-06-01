from django.urls import path


from .views import ReviewRetrieveUpdateDestroyView,ReviewListCreateView


urlpatterns=[
    path('review/',ReviewListCreateView.as_view(),name='review-create-list'),
    path('review/<int:pk>/',ReviewRetrieveUpdateDestroyView.as_view(),name='review-retrieve-update-destroy')
]