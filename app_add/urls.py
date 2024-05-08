from rest_framework import routers

from .views  import AddViewSet

router = routers.DefaultRouter()
router.register(r'', AddViewSet, basename= 'add')

urlpatterns = router.urls