from django.urls import include, path
from rest_framework import routers
from .views import UserViewSet, UserCreateViewSet

app_name = 'users'

router = routers.SimpleRouter()
router.register(r'users', UserViewSet)
router.register(r'users', UserCreateViewSet)

urlpatterns = [
    path('', include(router.urls)),
]