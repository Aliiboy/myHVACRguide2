"""
core App config.

stockage variables globales
"""

from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _

class CoreConfig(AppConfig):
    """
    Stockage metadonnee.

    (voir doc django)
    """ 

    name = 'core'
    login_url = reverse_lazy('dashboard:login')


CORE_NAVIGATION = [
    {
        'label': _('Dashboard'),
        'icon': 'fas fa-list',
        'url_name': 'customer:profile_update',
    },
]