from ipaddress import IPv6Address, IPv4Address

from django.http import FileResponse, Http404
from django.http.response import HttpResponseRedirectBase, HttpResponseGone
from django.views.generic import TemplateView
from django.views.generic.base import View, RedirectView

from wolfizen_net.apps.main import util
from wolfizen_net.apps.main.util import CachedViewMixin


class RootPageView(CachedViewMixin, TemplateView):
    template_name = "main/root.html"

    def get_context_data(self, **kwargs):
        context = super(RootPageView, self).get_context_data(**kwargs)
        client_addr = util.get_client_address(self.request)
        context['request_is_ipv6'] = isinstance(client_addr, IPv6Address)
        context['request_is_ipv4'] = isinstance(client_addr, IPv4Address)
        return context


class InfiniteLinksView(CachedViewMixin, TemplateView):
    template_name = "main/infinite.html"

    def get_context_data(self, **kwargs):
        context = super(InfiniteLinksView, self).get_context_data(**kwargs)
        current_depth = int(context['depth'])
        context['depth'] = current_depth
        context['next_depth'] = current_depth + 1
        context['prev_depth'] = current_depth - 1
        return context


class PetRegistrationView(CachedViewMixin, TemplateView):
    template_name = "main/petregistration.html"

    def get_context_data(self, **kwargs):
        context = super(PetRegistrationView, self).get_context_data(**kwargs)

        if context['pet_id'].lower() == "tala":
            context['photo_path'] = \
                "main/2020-03-14_Elkir_spirit_of_the_forest_icon_1914.png"
            context['accent_color'] = "#5fb0ff"
            context['name'] = "Tala Luna"
            context['species'] = "Canis lupus"
            context['variant_meta_name'] = "Subspecies"
            context['variant'] = "Northwestern wolf"
            context['fur_color'] = "Gray"
            context['eye_color'] = "Amber"
            context['weight'] = "40 kg"

        elif context['pet_id'].lower() == "quill":
            context['photo_path'] = \
                "main/2021-08-19_Holt-Odium_Quill_Refsheet_BG_feral_icon_666.png"
            context['accent_color'] = "#4f367e"
            context['name'] = "Quill Luna"
            context['species'] = "Canis familiaris"
            context['variant_meta_name'] = "Breed"
            context['variant'] = "Border Collie"
            context['fur_color'] = "Black & white"
            context['eye_color'] = "Blue"
            context['weight'] = "17 kg"

        return context


class RainbowTextView(CachedViewMixin, TemplateView):
    template_name = "main/rainbow.html"


class FileView(CachedViewMixin, View):
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


class RedirectViewKeepMethod(RedirectView):

    def get(self, request, *args, **kwargs):
        url = self.get_redirect_url(*args, **kwargs)
        if url:
            if self.permanent:
                return HttpResponsePermanentRedirectKeepMethod(url)
            else:
                return HttpResponseRedirectKeepMethod(url)
        else:
            return HttpResponseGone()

    def dispatch(self, request, *args, **kwargs):
        return self.get(request, *args, **kwargs)


class HttpResponseRedirectKeepMethod(HttpResponseRedirectBase):
    status_code = 307


class HttpResponsePermanentRedirectKeepMethod(HttpResponseRedirectBase):
    status_code = 308
