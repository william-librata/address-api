from django.urls import path, include
from rest_framework.routers import SimpleRouter
from rest_framework.authtoken import views as authtokenviews

from places import views


router = SimpleRouter()
router.register(r'address', views.AddressViewSet, basename='address')
router.register(r'geocode', views.GeocodeAddressViewSet, basename='geocode')
router.register(r'geocodereliabilityaut', views.GeocodeReliabilityAutViewSet)
router.register(r'locality', views.LocalityViewSet)
router.register(r'localityclassaut', views.LocalityClassAutViewSet)
router.register(r'parse', views.ParseAddressViewSet, basename='parse')
router.register(r'state', views.StateViewSet)

urlpatterns = [
    path('api-token/', authtokenviews.obtain_auth_token),
    path('user/', views.UserList.as_view(), name='user-list'),
    path('', include(router.urls)),
    path('', views.APIRoot.as_view()),
]
