from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from places import views

urlpatterns = [
    path('state/', views.StateList.as_view()),
    path('state/<str:state_abbreviation>/', views.StateDetail.as_view())
]

urlpatterns = format_suffix_patterns(urlpatterns)