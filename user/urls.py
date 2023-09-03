from rest_framework.routers import DefaultRouter
from .views import Authentication

router = DefaultRouter()

router.register('auth', Authentication)

urlpatterns = router.urls