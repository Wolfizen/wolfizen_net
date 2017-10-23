from django.http import HttpResponseRedirect
from django.shortcuts import redirect
from django.urls import reverse_lazy, reverse
from django.views import View
from django.views.generic import CreateView
from django.views.generic.list import ListView

from wolfizen_net.apps.rsfa_voting.forms import CreateShowForm, VoteForm
from wolfizen_net.apps.rsfa_voting.models import Show, ShowVote


class ShowListView(ListView):
    template_name = "rsfa_voting/list_votes.html"
    model = Show

    def get_context_data(self, **kwargs):
        context = super(ShowListView, self).get_context_data(**kwargs)
        source_ip = get_client_ip(self.request)
        for show in context['object_list']:
            show.has_voted = ShowVote.objects.filter(show_id=show.id, source_ip=source_ip).exists()
        return context


class CreateShowView(CreateView):
    template_name = "rsfa_voting/create_show.html"
    form_class = CreateShowForm
    success_url = reverse_lazy('rsfa-voting:list-votes')

    def form_valid(self, form):
        # Duplicate code from super, to add code between save() and returning response
        self.object = form.save()
        ShowVote.objects.create(show=self.object, source_ip=get_client_ip(self.request))
        return HttpResponseRedirect(self.get_success_url())


class VoteView(View):
    success_url = reverse_lazy('rsfa-voting:list-votes')

    def post(self, request):
        source_ip = get_client_ip(self.request)
        print("Received vote from IP: {}".format(source_ip))
        form = VoteForm(request.POST)
        if form.is_valid():
            show = form.cleaned_data['show']
            if not ShowVote.objects.filter(show_id=show.id, source_ip=source_ip).exists():
                ShowVote.objects.create(source_ip=source_ip, show=show)
            else:
                print("Tried to vote for same show: {}".format(source_ip))
        else:
            # TODO
            print("Invalid form: {}".format(form.errors))
        return redirect(reverse('rsfa-voting:list-votes'))


def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        return x_forwarded_for.split(',')[-1].strip()
    elif request.META.get('HTTP_X_REAL_IP'):
        return request.META.get('HTTP_X_REAL_IP')
    else:
        return request.META.get('REMOTE_ADDR')
