from rest_framework import routers
from .api import DailystatusViewset

router = routers.DefaultRouter()
router.register('api/status', DailystatusViewset, 'status')

urlpatterns = router.urls