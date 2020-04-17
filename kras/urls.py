from rest_framework import routers
from .api import KraViewset

router = routers.DefaultRouter()
router.register('api/kra', KraViewset, 'Kra')

urlpatterns = router.urls
