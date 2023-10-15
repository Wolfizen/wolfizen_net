import os

from django.conf import settings
from django.templatetags.static import static
from django.urls import path, re_path

from wolfizen_net.apps.main.views import *


app_name = "main"
urlpatterns = [
    path(
        "",
        RootPageView.as_view(),
        name="root",
    ),
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
    path(
        "rainbow",
        RainbowTextView.as_view(),
        name="rainbow-text"
    ),
    # Asset aliases
    path(
        "resume.pdf",
        RedirectViewKeepMethod.as_view(
            url=static("main/Resumé.pdf"),
            permanent=False),
        name="resume",
    ),
    path(
        "refsheet",
        RedirectViewKeepMethod.as_view(
            url=static("main/2022-02-12_Holt-Odium_Refsheet_Standard_5400.png"),
            permanent=False),
        name="resume",
    ),
    path(
        "refsheet-nsfw",
        RedirectViewKeepMethod.as_view(
            url=static("main/2022-02-12_Holt-Odium_Refsheet_Extended_5400.png"),
            permanent=False),
        name="resume",
    ),
    # External redirects
    path(
        "ddnswolf",
        RedirectViewKeepMethod.as_view(
            url="https://github.com/Wolfizen/DDNSWolf",
            permanent=False),
        name="ddnswolf",
    ),
]
