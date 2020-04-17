from rest_framework import routers
from .api import KrasheetViewset

router = routers.DefaultRouter()
router.register('api/krasheet', KrasheetViewset, 'Krasheet')

urlpatterns = router.urls
