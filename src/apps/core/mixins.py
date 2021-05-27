"""
core mixins.

heritage
"""

# > Django
from django.views.generic.base import ContextMixin


class PageTitleMixin(ContextMixin):
    """
    PageTitleMixin.

    Passe les objets en context
    utile pour onglets de navigation et fil d'Ariane
    Les titres de page dynamiques sont possibles en remplaçant get_page_title.
    """

    page_title = None
    page_subtitle = None
    sidebar_active_link = None
    sidebar_dropdown_show = None
    active_tab = None

    def get_page_title(self):
        return self.page_title

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx.setdefault('page_title', self.get_page_title())
        ctx.setdefault('page_subtitle', self.page_subtitle)
        ctx.setdefault('sidebar_active_link', self.sidebar_active_link)
        ctx.setdefault('sidebar_dropdown_show', self.sidebar_dropdown_show)
        ctx.setdefault('active_tab', self.active_tab)
        return ctx
