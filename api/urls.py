from django.conf.urls import url, include
from rest_framework import routers
from accounts.views import UserViewSet
from rest_framework_jwt.views import obtain_jwt_token

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    url(r'^api-token-auth/', obtain_jwt_token),
    url(r'^', include(router.urls)),
]
