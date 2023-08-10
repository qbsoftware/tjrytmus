from django.utils.translation import ugettext_lazy as _
from leprikon.site.settings import *

# Application definition
INSTALLED_APPS = (
    [
        "tjrytmus",
    ]
    + INSTALLED_APPS
    + [
        "cms_articles",
        "django.contrib.redirects",
        "aldryn_search",
    ]
)

# search settings
HAYSTACK_CONNECTIONS = {
    "default": {
        "ENGINE": "haystack.backends.whoosh_backend.WhooshEngine",
        "PATH": os.path.join(BASE_DIR, "data", "search"),
    },
    "cs": {
        "ENGINE": "haystack.backends.whoosh_backend.WhooshEngine",
        "PATH": os.path.join(BASE_DIR, "data", "search"),
    },
}

CMS_ARTICLES_TEMPLATES = [
    ("cms_articles/default.html", _("Default")),
    ("cms_articles/galerie.html", "Galerie"),
]

DJANGOCMS_FILE_TEMPLATES = [
    ("jumbotron", _("Jumbotron")),
]
