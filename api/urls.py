from django.conf.urls import url, include
# from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token
from rest_framework import routers

from accounts.views import UserViewSet, TokenAuthView
from stores.views import StoreViewSet, StoreRVViewSet

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'stores', StoreViewSet)
router.register(r'store-review', StoreRVViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    # AT THE MOMENT, JWT DOESN'T WORKS WITH SWAGGER YET
    # url(r'^token-auth/', obtain_jwt_token),
    # url(r'^token-refresh/', refresh_jwt_token),

    # USE DEFAULT DRF TOKEN IN DB
    url(r'^token/', TokenAuthView.as_view({'post': 'create'})),
    url(r'^', include(router.urls)),
]
