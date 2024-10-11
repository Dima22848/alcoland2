from django.urls import path, include
from .views import *
from django.conf import settings
from django.conf.urls.static import static

from rest_framework import routers

router = routers.SimpleRouter()
router.register(r'alcogol', AlcogolViewSet)

urlpatterns = [
    path('api/v1/', include(router.urls)), #http://127.0.0.1:8000/api/v1/alcogol/,
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)