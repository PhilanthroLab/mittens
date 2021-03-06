import pprint

from django.core.mail import EmailMessage

import log
from rest_framework.reverse import reverse
from sesame.utils import get_query_string


def send_login_email(user, request, *, welcome):
    assert user.email, f"User has no email: {user}"

    if welcome:
        subject = "Vote with Mittens"
    else:
        subject = "Greetings from Mittens"

    message = EmailMessage(
        subject=subject,
        from_email="Citizen Labs <noreply@citizenlabs.org>",
        to=[user.email],
    )
    if welcome:
        message.template_id = 'voter-engagement-welcome'
    else:
        message.template_id = 'voter-engagement-login'

    message.merge_global_data = {
        'FIRST_NAME': user.first_name,
        'LAST_NAME': user.last_name,
        'LOGIN_URL': get_login_url(request, user),
        'SITE_URL': get_site_url(request),
        'UNSUBSCRIBE_URL': get_unsubscribe_url(request, user),
        'ABOUT_URL': 'https://citizenlabs.org/about/',
    }

    log.debug(f"Sending email: {prettify(message.__dict__)}")
    count = message.send(fail_silently=False)

    return count


def get_login_url(request, user):
    base = reverse('redirector', args=["login"], request=request)
    token = get_query_string(user)
    return base + token


def get_site_url(request):
    return reverse('index', request=request)


def get_unsubscribe_url(request, user):
    base = reverse('redirector', args=["unsubscribed"], request=request)
    token = get_query_string(user)
    return base + token + "&unsubscribe=true"


def prettify(data: dict):
    return "{\n " + pprint.pformat(data, indent=2)[1:-1] + ",\n}"
