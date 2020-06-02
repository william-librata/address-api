from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from django.views.generic import TemplateView
from rest_framework.schemas import get_schema_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('places.urls'), name='places-urls'),
    path('', include('rest_framework.urls')),
    path('swagger-ui/', TemplateView.as_view(
            template_name='swagger-ui.html',
            extra_context={'schema_url':'openapi-schema'}
        ), name='swagger-ui'),
    path('openapi', get_schema_view(
            title='Places API',
            description='API to get address and places information',
            version='0.0.1',
            urlconf='api.urls',
        ), name='openapi-schema'),
]
