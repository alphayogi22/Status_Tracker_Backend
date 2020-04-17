from rest_framework import routers
from .api import DailytaskViewset

router = routers.DefaultRouter()
router.register('api/task', DailytaskViewset, 'task')

urlpatterns = router.urls
