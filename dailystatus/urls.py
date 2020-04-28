from rest_framework import routers
from .views import DailyStatusViewSet

router = routers.DefaultRouter()
router.register('api/status', DailyStatusViewSet, 'status')

urlpatterns = router.urls