from rest_framework import routers
from .api import DailyuserViewSet

router = routers.DefaultRouter()
router.register('api/users', DailyuserViewSet, 'users')

urlpatterns = router.urls