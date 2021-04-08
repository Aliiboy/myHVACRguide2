"""
core adapter.

Modifie le comportement de Django-allauth
"""

# > Django
from django import forms
from django.contrib.sites.shortcuts import get_current_site
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
# > Django-allauth
from allauth.account.adapter import DefaultAccountAdapter
# > Models
from core.models import (
    CustomSite,
)
# > Settings
from myhvacrguide.settings import base as settings


class MyAccountAdapter(DefaultAccountAdapter):
    """
    Django-allauth.

    remplacement des méthodes d'adaptateur
    """

    def is_open_for_signup(self, request):
        """
        ON/OFF Inscription.

        Vérifie si le site est ouvert aux inscriptions ou non
        va chercher le field signup de CustomSite
        en fonction du SITE_ID en cours
        """
        current_site_id = get_current_site(request).id

        try:
            site_id = CustomSite.objects.get(site=current_site_id)
            if site_id.signup:
                return True
            else:
                return False
        except CustomSite.DoesNotExist:
            print("Oops!  Veuillez creer le OneToOne"
                  "avec le site pour les inscriptions...")
            return False

    def clean_email(self, email):
        """
        Domaine autorisé.

        Vérifie lors de l'inscription que le domaine
        est dans la liste définie.
        """
        email = super().clean_email(email)
        if email.endswith(settings.ACCOUNT_SIGNUP_EMAIL_DOMAIN_ALLOWED):
            return email
        raise forms.ValidationError(_("Ce domaine e-mail n'est pas "
                                      "autorisé sur ce site."))

    def respond_user_inactive(self, request, user):
        """
        Compte inactif.

        Renvoie vers la page correspondante
        """
        return HttpResponseRedirect(
            reverse('customer:account_inactive'))
