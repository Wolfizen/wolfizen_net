from django.db.models import Count, F, Subquery, Sum, Case, When
from django.http import HttpResponseRedirect
from django.shortcuts import redirect
from django.urls import reverse_lazy, reverse
from django.views import View
from django.views.generic import TemplateView, CreateView
from django.views.generic.list import ListView

from wolfizen_net.forms import CreateShowForm, VoteForm
from wolfizen_net.models import Show, ShowVote


class RootPageView(TemplateView):
    template_name = "wolfizen_net/root.html"


class InfiniteRecursionView(TemplateView):
    template_name = "wolfizen_net/infinite.html"

    def get_context_data(self, **kwargs):
        context = super(InfiniteRecursionView, self).get_context_data(**kwargs)
        context['depth'] = int(context['depth'])
        context['next_depth'] = context['depth'] + 1
        context['prev_depth'] = context['depth'] - 1
        return context


class RainbowTextView(TemplateView):
    template_name = "wolfizen_net/rainbow.html"


class ShowListView(ListView):
    template_name = "wolfizen_net/rsfa_voting.html"
    model = Show

    def get_context_data(self, **kwargs):
        context = super(ShowListView, self).get_context_data(**kwargs)
        source_ip = get_client_ip(self.request)
        for show in context['object_list']:
            show.has_voted = ShowVote.objects.filter(show_id=show.id, source_ip=source_ip).exists()
        return context


class CreateShowView(CreateView):
    template_name = "wolfizen_net/create_show.html"
    form_class = CreateShowForm
    success_url = reverse_lazy('rsfa-voting')

    def form_valid(self, form):
        # Duplicate code from super, to add code between save() and returning response
        self.object = form.save()
        ShowVote.objects.create(show=self.object, source_ip=get_client_ip(self.request))
        return HttpResponseRedirect(self.get_success_url())


class VoteView(View):
    success_url = reverse_lazy('rsfa-voting')

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
        return redirect(reverse('rsfa-voting'))


def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        return x_forwarded_for.split(',')[-1].strip()
    elif request.META.get('HTTP_X_REAL_IP'):
        return request.META.get('HTTP_X_REAL_IP')
    else:
        return request.META.get('REMOTE_ADDR')
