from django.urls import path, include
from rest_framework.routers import SimpleRouter
from rest_framework.authtoken import views as authtokenviews

from places import views


router = SimpleRouter()
router.register(r'address', views.AddressViewSet, basename='address')
router.register(r'geocodereliabilityaut', views.GeocodeReliabilityAutViewSet)
router.register(r'locality', views.LocalityViewSet)
router.register(r'localityclassaut', views.LocalityClassAutViewSet)
router.register(r'state', views.StateViewSet)

urlpatterns = [
    path('api-token/', authtokenviews.obtain_auth_token),
    path('user/', views.UserList.as_view(), name='user-list'),
    path('user/<str:username>/', views.UserDetail.as_view(), name='user-detail'),
    path('parse/<path:address>/', views.ParseAddress.as_view(), name='parse-address'),
    path('geocode/<path:address>/', views.GeocodeAddress.as_view(), name='geocode-address'),
    path('', include(router.urls)),
    path('', views.APIRoot.as_view()),
]
