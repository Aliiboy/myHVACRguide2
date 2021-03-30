"""
customer views.

Vues
"""

# > Django
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _
from django.views import generic
# > Forms
from customer.forms import (
    AccountsSettingsForm,
)


class AccountsSettingsView(LoginRequiredMixin, generic.FormView):
    """
    Account Settings.

    Edition du profil utilisateur
    """

    form_class = AccountsSettingsForm
    template_name = 'pages/customer/account_settings.html'
    success_url = reverse_lazy('customer:account_settings')

    def get_form_kwargs(self):
        """
        Paramètres.

        Construit les paramètres nommés requis
        pour créer une instance de formulaire.
        """
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

    def form_valid(self, form):
        """
        Conformite du formulaire.

        Si le formulaire est valide, redirigez vers l'URL fournie.
        """
        form.save()
        messages.success(self.request, _("Profil mis à jour"))
        return redirect(self.get_success_url())
