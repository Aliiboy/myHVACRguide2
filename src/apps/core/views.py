"""
core views.

Vues
"""

# > Django
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils.translation import gettext_lazy as _
from django.views import generic

# > Import
from core.mixins import (
    PageTitleMixin,
)


class IndexUiView(LoginRequiredMixin,
                  generic.TemplateView,
                  PageTitleMixin,
                  ):
    """
    IndexUiView.

    Dashboard utilisateur
    """

    template_name = "pages/core/index.html"
    # Mixins PageTitleMixin
    page_title = _("Acceuil")
    sidebar_active_link = 'ui_index'
    sidebar_dropdown_show = None
    active_tab = None
