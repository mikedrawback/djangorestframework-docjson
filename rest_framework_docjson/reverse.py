"""
Provide a reverse function that wraps the url in the DocJSON link format
"""
from rest_framework.reverse import reverse as rest_framework_reverse


def reverse(viewname, args=None, kwargs=None, request=None, format=None, **extra):
    """
    Same as `rest_framework.reverse.reverse`,
    but wraps the returned url in the DocJSON link format.
    """
    return {
        '_type': 'link',
        'url': rest_framework_reverse(viewname, args=args, kwargs=kwargs, request=request, format=format, **extra)
    }
