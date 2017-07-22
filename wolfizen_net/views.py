from django.views.generic import TemplateView


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
