from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework.routers import DefaultRouter
from places import views


router = DefaultRouter()
#router.register(r'state', views.StateViewSet)
router.register(r'locality', views.LocalityViewSet)
router.register(r'localityclassaut', views.LocalityClassAutViewSet)
router.register(r'geocodereliabilityaut', views.GeocodeReliabilityAutViewSet)
'''
urlpatterns = [
    path('', views.APIRoot.as_view()),
    path('user/', views.UserList.as_view(), name='user-list'),
    path('user/<str:username>/', views.UserDetail.as_view(), name='user-detail'),
    path('state/', views.StateList.as_view(), name='state-list'),
    path('state/<str:state_abbreviation>/', views.StateDetail.as_view(), name='state-detail'),
    path('', include(router.urls)),
]


urlpatterns = format_suffix_patterns(urlpatterns)
'''


urlpatterns = [
    path('state/', views.StateList.as_view(), name='state-list'),
    path('state/<str:state_pid>/', views.StateDetail.as_view(), name='state-detail'),
    path('', include(router.urls)),
]
