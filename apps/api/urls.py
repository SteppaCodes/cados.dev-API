from django.urls import path

from .views import (APIHomeView, AdvocatesListView,AdvocateDetailView, 
                    CompaniesListView, CompanyDetailView)

urlpatterns = [
    #companies URl
    path("companies/", CompaniesListView.as_view()),
    path("companies/<str:name>", CompanyDetailView.as_view(), name="company-detail"),

    path("", APIHomeView.as_view()),
    path("advocates/", AdvocatesListView.as_view()),
    path("advocates/<int:id>/", AdvocateDetailView.as_view(), name="advocate-detail"),

]