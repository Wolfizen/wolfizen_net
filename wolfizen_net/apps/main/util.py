import traceback
from ipaddress import ip_address, IPv4Address, IPv6Address
from typing import Union

from django.conf import settings
from django.views.generic.base import View


class CachedViewMixin(View):
    """
    Adds a Cache-Control header to the response.
    https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Cache-Control

    self.max_age: The cache duration of the page, in seconds. Default is settings.CACHE_CONTROL_DEFAULT_MAX_AGE.
    self.cacheability: Who should cache this page. Default is 'public'.
    """

    max_age = None
    cacheability = None

    def dispatch(self, request, *args, **kwargs):
        """Wraps the default Django dispatch() to modify the response headers."""

        max_age = self.max_age if self.max_age is not None else settings.CACHE_CONTROL_DEFAULT_MAX_AGE
        cacheability = self.cacheability if self.cacheability is not None else 'public'

        response = super(CachedViewMixin, self).dispatch(request, *args, **kwargs)
        response['Cache-Control'] = "{},max-age={}".format(cacheability, max_age)
        return response


def get_client_address(request) -> Union[IPv4Address, IPv6Address, None]:
    try:
        potential_addresses = [
            request.headers.get('X-Real-IP'),
            request.META.get('REMOTE_ADDR')]
        address = next(filter(lambda x: x is not None, potential_addresses))
        return ip_address(address)
    except (ValueError, StopIteration) as ex:
        traceback.print_exception(type(ex), ex, ex.__traceback__, chain=True)
        return None
