from django.conf.urls import url, include
from rest_framework import routers
from api.views import UserViewSet, GroupViewSet, TokenAuthView, Logout

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'groups', GroupViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    url(r'^api-auth/', TokenAuthView.as_view({'post': 'create'})),
    url(r'^', include(router.urls)),
]
