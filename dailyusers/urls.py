from rest_framework.routers import DefaultRouter
from django.conf.urls import include, re_path
from .views import DailyUserViewSet

router = DefaultRouter()
router.register('api/users', DailyUserViewSet, 'users')

urlpatterns = [
    re_path('^', include(router.urls)),
]