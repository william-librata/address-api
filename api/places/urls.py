from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework.routers import DefaultRouter
from places import views


router = DefaultRouter()
router.register(r'locality', views.LocalityViewSet)
router.register(r'state', views.StateViewSet)
router.register(r'localityclassaut', views.LocalityClassAutViewSet)
router.register(r'geocodereliabilityaut', views.GeocodeReliabilityAutViewSet)


urlpatterns = [
    path('', include(router.urls)),
]
