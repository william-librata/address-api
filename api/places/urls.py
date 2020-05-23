from django.urls import path, include
from rest_framework.routers import SimpleRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView

from places import views


router = SimpleRouter()
router.register(r'parseaddress', views.ParseAddressViewSet, basename='parseaddress')
router.register(r'locality', views.LocalityViewSet)
router.register(r'state', views.StateViewSet)
router.register(r'localityclassaut', views.LocalityClassAutViewSet)
router.register(r'geocodereliabilityaut', views.GeocodeReliabilityAutViewSet)
router.register(r'geocodeaddress', views.GeocodeAddressViewSet, basename='geocodeaddress')


urlpatterns = [
    #path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    #path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    #path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('user/', views.UserList.as_view(), name='user-list'),
    path('', include(router.urls)),
    path('', views.APIRoot.as_view()),
]
