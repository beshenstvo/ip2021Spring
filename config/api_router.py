from django.conf import settings
from rest_framework.routers import DefaultRouter, SimpleRouter

from clean_burg.main.api.views import OrderViewSet, ServiceViewSet
from clean_burg.users.api.views import UserViewSet

if settings.DEBUG:
    router = DefaultRouter()
else:
    router = SimpleRouter()

router.register("users", UserViewSet)
router.register("orders", OrderViewSet)
router.register("services", ServiceViewSet)

app_name = "api"
urlpatterns = router.urls
