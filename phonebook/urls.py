from .views import ContactViewSet
from rest_framework.routers import DefaultRouter


router = DefaultRouter()

router.register('contact', ContactViewSet)

urlpatterns = router.urls

