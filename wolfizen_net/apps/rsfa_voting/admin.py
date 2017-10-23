from django.contrib import admin

from wolfizen_net.apps.rsfa_voting.models import Show, ShowVote

admin.site.register(Show)
admin.site.register(ShowVote)
