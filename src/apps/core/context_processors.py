"""
core Context processor.

ajouter des variables aux contextes des templates
"""

# > Settings
from core.apps import CORE_SITE_NAME


def metadata(request):
    """
    Metadata.

    Ajoute des metadonnees a passer au template
    """
    return {'site_name': CORE_SITE_NAME,
            }
