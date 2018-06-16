from django.views.generic import TemplateView


class RootPageView(TemplateView):
    template_name = "main/root.html"


class InfiniteRecursionView(TemplateView):
    template_name = "main/infinite.html"

    def get_context_data(self, **kwargs):
        context = super(InfiniteRecursionView, self).get_context_data(**kwargs)
        current_depth = int(context['depth'])
        context['depth'] = current_depth
        context['next_depth'] = current_depth + 1
        context['prev_depth'] = current_depth - 1
        return context


class RainbowTextView(TemplateView):
    template_name = "main/rainbow.html"
