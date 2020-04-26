from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin

urlpatterns = [
    url(r"^", include('wolfizen_net.apps.main.urls')),
    url(r"^deep-listening/", include('wolfizen_net.apps.deeplistening.urls')),
    # url(r"^admin/", admin.site.urls),
]

# Serve media files in debug mode, just like static files.
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
