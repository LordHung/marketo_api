"""marketo_api URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.conf import settings
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static

from rest_framework_swagger.views import get_swagger_view
from rest_framework import routers
from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token
from rest_framework.documentation import include_docs_urls

from accounts.views import UserViewSet, TokenAuthView
from stores.views import StoreViewSet, StoreRVViewSet, StoreAPIView

from . import schema_generator

# schema_view = get_swagger_view(title='Marketo API')  # Default schema_view Swagger
# schema_view = schema_generator.get_swagger_view(title='Marketo API')  # Customer schema_view

router = routers.DefaultRouter()
router.register(r'api/users', UserViewSet)
router.register(r'api/stores', StoreViewSet)
router.register(r'api/store-reviews', StoreRVViewSet)

urlpatterns = [
    url(r'^api/token/', obtain_jwt_token),
    url(r'^api/refresh-token/', refresh_jwt_token),
    url(r'^auth/', include('rest_framework.urls')),  # Default authen of DRF
    # url(r'^api/token/', TokenAuthView.as_view({'post': 'create'})),
    # url(r'^api/stores/', StoreAPIView.as_view(), name='store_index'),
    # url(r'^logout/', Logout.as_view()),
]

urlpatterns += [
    url(r'^swagger/', schema_view, name='home'),
    url(r'^docs/', include_docs_urls(title='Marketo API', description='xxxxx', public=False)),
    url(r'^', include(router.urls)),
    url(r'^admin/', admin.site.urls),
]

# DEVELOPMENT SERVE STATICFILES
if settings.DEBUG:
    urlpatterns += staticfiles_urlpatterns()
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
