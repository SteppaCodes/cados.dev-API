from django.urls import path

from .views import (APIHomeView, AdvocatesListView,AdvocateDetailView)

urlpatterns = [
    path("", APIHomeView.as_view()),
    path("advocates/", AdvocatesListView.as_view()),
    path("advocates/<int:id>/", AdvocateDetailView.as_view()),
]