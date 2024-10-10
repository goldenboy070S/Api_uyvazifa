from .views import *
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('video', VideoViewSet)

urlpatterns = router.urls