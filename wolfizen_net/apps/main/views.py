from django.http import FileResponse, Http404
from django.views.generic import TemplateView
from django.views.generic.base import View


class RootPageView(TemplateView):
    template_name = "main/root.html"


class InfiniteLinksView(TemplateView):
    template_name = "main/infinite.html"

    def get_context_data(self, **kwargs):
        context = super(InfiniteLinksView, self).get_context_data(**kwargs)
        current_depth = int(context['depth'])
        context['depth'] = current_depth
        context['next_depth'] = current_depth + 1
        context['prev_depth'] = current_depth - 1
        return context


class RainbowTextView(TemplateView):
    template_name = "main/rainbow.html"


class FileView(View):
    """
    This custom view will serve any specified file.

    as_view() accepts two arguments:
        file_path: The path to the file. Recommended to use `os.path.join(TEMPLATE_DIR, ...)`
        content_type: Passed into FileResponse().
    """

    file_path = None
    content_type = None

    def get(self, request, *args, **kwargs):
        try:
            return FileResponse(open(self.file_path, 'rb'), content_type=self.content_type)
        except FileNotFoundError:
            raise Http404()
