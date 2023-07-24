from ipaddress import IPv6Address, IPv4Address
from typing import Any

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
    template_name = "main/pet-registration.html"

    pets: dict[str, dict[str, Any]] = {
        "tala": {
            "name": "Tala Luna",
            "species": "Canis lupus",
            "variant": "Northwestern wolf",
            "variant_meta_name": "Subspecies",
            "fur_color": "Gray",
            "eye_color": "Amber",
            "weight": "40 kg",
            "photo_path": "main/2020-03-14_Elkir_spirit_of_the_forest_icon_1914.png",
            "accent_color": "#5fb0ff",
        },
        "quill": {
            "name": "Quill Luna",
            "species": "Canis familiaris",
            "variant": "Border Collie",
            "variant_meta_name": "Breed",
            "fur_color": "Black & white",
            "eye_color": "Blue",
            "weight": "17 kg",
            "photo_path": "main/2021-08-19_Holt-Odium_Quill_Refsheet_BG_feral_icon_666.png",
            "accent_color": "#4f367e",
        },
    }

    def get_context_data(self, **kwargs):
        context = super(PetRegistrationView, self).get_context_data(**kwargs)

        pet_id = context.get("pet_id", "")
        if pet_id in self.pets:
            context.update(self.pets[pet_id])

        return context


class RainbowTextView(CachedViewMixin, TemplateView):
    template_name = "main/rainbow.html"


class FileView(CachedViewMixin, View):
    """
    This custom view will serve any specified file.

    as_view() accepts two arguments:
        file_path: The path to the file. Recommended: `os.path.join(TEMPLATE_DIR, ...)`
        content_type: The MIME-type of the file.
    """

    file_path = None
    content_type = None

    def get(self, request, *args, **kwargs):
        try:
            return FileResponse(
                open(self.file_path, 'rb'),
                content_type=self.content_type)
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
