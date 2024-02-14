from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


from .views import (APIHomeView, AdvocatesListView,AdvocateDetailView, 
                    CompaniesListView, CompanyDetailView)

urlpatterns = [

    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),

    #companies URl
    path("companies/", CompaniesListView.as_view()),
    path("companies/<str:name>", CompanyDetailView.as_view(), name="company-detail"),

    path("home", APIHomeView.as_view()),
    path("advocates/", AdvocatesListView.as_view()),
    path("advocates/<int:id>/", AdvocateDetailView.as_view(), name="advocate-detail"),

]