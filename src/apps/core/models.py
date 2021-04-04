"""
core models.

Models comprenant :
    - Site
"""

# > Django
from django.db import models
from django.utils.translation import gettext_lazy as _
# > Django Models
from django.contrib.sites.models import Site


class CustomSite(models.Model):
    """
    Site.

    necessite une relation OneToOne avec models.Site
    pour ajouter des champs supplémentaires.
    Une instance de Site n'extend pas, il recreer...
    """

    site = models.OneToOneField(
        Site, verbose_name=_('Site'),
        related_name='custom_site', on_delete=models.CASCADE
    )
    signup = models.BooleanField(
        verbose_name=_('Inscription'),
        default=False,
        help_text=_(
            "Designe la permission de s'inscrire "
            "sur le site."
        ),
    )

    class Meta:  # noqa
        abstract = False
        app_label = 'core'
        # db_table = ''
        verbose_name = _('Site')
        verbose_name_plural = _('Sites')

    def __str__(self):  # noqa
        return _("Extension de '%s'") % self.site
