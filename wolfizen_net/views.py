from django.views.generic import TemplateView


class RootPageView(TemplateView):
    template_name = "wolfizen_net/root.html"
