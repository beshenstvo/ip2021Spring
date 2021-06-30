from django.conf import settings

from clean_burg.main.models import Service


def settings_context(_request):
    """Settings available by default to the templates context."""
    # Note: we intentionally do NOT expose the entire settings
    # to prevent accidental leaking of sensitive information
    return {"DEBUG": settings.DEBUG}


def services_context(request):
    services = Service.objects.values("name")
    return {"services": services}
