"""
Mixin Response
"""
from __future__ import unicode_literals

from .decorators import ajax


class AJAXMixin(object):
    """
    AJAX Mixin Class
    """
    ajax_mandatory = True

    def dispatch(self, request, *args, **kwargs):
        """
        Using ajax decorator
        """
        return ajax(mandatory=self.ajax_mandatory)(super(
            AJAXMixin, self).dispatch)(request, *args, **kwargs)
