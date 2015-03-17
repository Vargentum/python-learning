from django.conf import settings


def common_values(request):
    return {
        'common': {
            'SITE_NAME': settings.SITE_NAME
        }
    }
