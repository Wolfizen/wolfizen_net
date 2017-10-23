from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r"^", include('wolfizen_net.apps.main.urls')),
    url(r"^rsfa-voting/", include('wolfizen_net.apps.rsfa_voting.urls')),
    url(r"^admin/", admin.site.urls),
]
