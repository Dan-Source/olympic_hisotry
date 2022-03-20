from django.conf import settings
from django.urls import path, re_path, include, reverse_lazy
from django.conf.urls.static import static
from django.contrib import admin
from django.views.generic.base import RedirectView
from rest_framework.routers import SimpleRouter
from rest_framework.authtoken import views
from rest_framework import permissions

from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="Olympic API",
        default_version='v1',
        description="Olympic API",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="dan.dluis.dl@gmail.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

system_url = [
    path('admin/', admin.site.urls),
    re_path(r'^swagger(?P<format>\.json|\.yaml)$',
        schema_view.without_ui(cache_timeout=0), name='schema-json'),
    re_path(r'^swagger/$', schema_view.with_ui('swagger',
        cache_timeout=0), name='schema-swagger-ui'),
    re_path(r'^redoc/$', schema_view.with_ui('redoc',
        cache_timeout=0), name='schema-redoc'),
]

urlpatterns = [
    path('api/v1/', include('olympic_history.users.urls')),
    path('api/v1/olympic/', include('olympic_history.olympic.urls')),
    path('api-token-auth/', views.obtain_auth_token),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),

] + system_url + \
    static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
