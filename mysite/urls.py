from django.conf.urls import include, url, static
from django.conf import settings

urlpatterns = [
    url(r'^core/', include('core.urls', namespace='core'))
] + static.static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
