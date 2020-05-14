from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from places import views

urlpatterns = [
    path('', views.APIRoot.as_view()),
    path('user/', views.UserList.as_view(), name='user-list'),
    path('user/<str:username>/', views.UserDetail.as_view(), name='user-detail'),
    path('state/', views.StateList.as_view(), name='state-list'),
    path('state/<str:state_abbreviation>/', views.StateDetail.as_view(), name='state-detail'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
