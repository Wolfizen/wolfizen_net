from django.conf.urls import url
from django.views.decorators.csrf import csrf_exempt

from wolfizen_net.apps.rsfa_voting.views import *

app_name = "rsfa-voting"
urlpatterns = [
    url(r"^$", ShowListView.as_view(), name="list-votes"),
    url(r"^new/$", CreateShowView.as_view(), name="new-show"),
    url(r"^vote/$", csrf_exempt(VoteView.as_view()), name="vote"),
]
