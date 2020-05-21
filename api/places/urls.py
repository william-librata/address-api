from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework.routers import DefaultRouter

from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView

from places import views


router = DefaultRouter()
router.register(r'locality', views.LocalityViewSet)
router.register(r'state', views.StateViewSet)
router.register(r'localityclassaut', views.LocalityClassAutViewSet)
router.register(r'geocodereliabilityaut', views.GeocodeReliabilityAutViewSet)


urlpatterns = [
    #path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    #path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    #path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('user/', views.UserList.as_view(), name='user-list'),
    path('', include(router.urls)),
]
