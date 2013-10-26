from django.conf import settings

def global_settings(request):
    """
    Returns global application settings necessary for template rendering
    """
    return dict(
        ASSET_URL=settings.ASSET_URL,
        mustache="{{",
        end_mustache="}}"
    )
