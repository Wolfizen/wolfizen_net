from django.conf.urls import url

from wolfizen_net.apps.deeplistening.views import *


app_name = "deeplistening"
urlpatterns = [
    url(r"^generative-composition", GenerativeCompositionView.as_view(), name="generative-composition"),
]
