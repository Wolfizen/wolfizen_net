import os

from django.conf import settings
from django.urls import path, re_path

from wolfizen_net.apps.main.views import *


app_name = "main"
urlpatterns = [
    path("", RootPageView.as_view(), name="root"),
    re_path(
        r"^infinite/(?P<depth>\d+)$",
        InfiniteLinksView.as_view(),
        name="infinite-links",
    ),
    re_path(
        r"^pet-registration/(?P<pet_id>\w+)$",
        PetRegistrationView.as_view(),
        name="pet-registration",
    ),
    path("rainbow", RainbowTextView.as_view(), name="rainbow-text"),
    path(
        "resume.pdf",
        FileView.as_view(
            file_path=os.path.join(settings.TEMPLATE_DIR, "main/Resumé.pdf"),
            content_type="application/pdf"),
        name="resume",
    ),
    # Redirects
    path(
        "refsheet",
        RedirectViewKeepMethod.as_view(
            url="https://imgur.com/a/RzMJatp", permanent=False),
        name="refsheet",
    ),
    path(
        "ddnswolf",
        RedirectViewKeepMethod.as_view(
            url="https://github.com/Wolfizen/DDNSWolf", permanent=False),
        name="ddnswolf",
    ),
]
