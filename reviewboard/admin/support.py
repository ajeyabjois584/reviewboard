from __future__ import unicode_literals

import base64
import time
from datetime import datetime
from hashlib import sha1

from django.conf import settings
from django.contrib.auth.models import User
from djblets.siteconfig.models import SiteConfiguration

from reviewboard import get_package_version


def get_install_key():
    """Returns the installation key for this server."""
    return sha1(settings.SECRET_KEY).hexdigest()


def serialize_support_data(request=None, force_is_admin=False):
    """Serializes support data into a base64-encoded string."""
    siteconfig = SiteConfiguration.objects.get_current()

    is_admin = (force_is_admin or
                (request is not None and request.user.is_staff))

    return base64.b64encode('\t'.join([
        get_install_key(),
        '%d' % is_admin,
        siteconfig.site.domain,
        siteconfig.get('site_admin_name'),
        siteconfig.get('site_admin_email'),
        get_package_version(),
        '%d' % User.objects.filter(is_active=True).count(),
        '%d' % int(time.mktime(datetime.now().timetuple())),
        siteconfig.get('company'),
    ]))


def get_default_support_url(request=None, force_is_admin=False):
    """Returns the URL for the default Review Board support page."""
    siteconfig = SiteConfiguration.objects.get_current()

    if siteconfig.get('send_support_usage_stats'):
        support_data = serialize_support_data(request, force_is_admin)
    else:
        support_data = ''

    return settings.DEFAULT_SUPPORT_URL % {
        'support_data': support_data,
    }


def get_register_support_url(request=None, force_is_admin=False):
    """Returns the URL for registering the Review Board support page."""
    siteconfig = SiteConfiguration.objects.get_current()

    if siteconfig.get('send_support_usage_stats'):
        support_data = serialize_support_data(request, force_is_admin)
    else:
        support_data = ''

    return settings.REGISTER_SUPPORT_URL % {
        'support_data': support_data,
    }


def get_support_url(request):
    """Returns the URL for the configured support page."""
    siteconfig = SiteConfiguration.objects.get_current()

    return (siteconfig.get('support_url') or
            get_default_support_url(request))
