import re
from visits.models import BlacklistedIP, BlacklistedUserAgent


def update_visit_count(request, visit_count):
    """
    Evaluates a request, add a visit to the corresponding item counter if the request is not blacklisted.
    """
    if not _is_blacklisted(request):
        visit_count.increase_visit_count(commit=True)


def _is_blacklisted(request):
    ip = _get_ip(request)
    user_agent = request.META.get('HTTP_USER_AGENT', '')[:255]

    return bool(
        BlacklistedIP.objects.filter(ip__exact=ip) or \
        BlacklistedUserAgent.objects.filter(user_agent__exact=user_agent)
    )


# this is not intended to be an all-knowing IP address regex
IP_RE = re.compile('\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}')


def _get_ip(request):
    """
    Retrieves the remote IP address from the request data.  If the user is
    behind a proxy, they may have a comma-separated list of IP addresses, so
    we need to account for that.  In such a case, only the first IP in the
    list will be retrieved. Also, some hosts that use a proxy will put the
    REMOTE_ADDR into HTTP_X_FORWARDED_FOR.  This will handle pulling back the
    IP from the proper place.

    **NOTE** This function was taken from django-tracking (MIT LICENSE)
             http://code.google.com/p/django-tracking/
    """

    # if neither header contain a value, just use local loopback
    ip_address = request.META.get('HTTP_X_FORWARDED_FOR', request.META.get('REMOTE_ADDR', '127.0.0.1'))
    if ip_address:
        # make sure we have one and only one IP
        try:
            ip_address = IP_RE.match(ip_address)
            if ip_address:
                ip_address = ip_address.group(0)
            else:
                # no IP, probably from some dirty proxy or other device
                # throw in some bogus IP
                ip_address = '10.0.0.1'
        except IndexError:
            pass

    return ip_address