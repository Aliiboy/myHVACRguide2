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
# > Views django-allauth
from allauth.account.views import (
    # SignupView,
    # LoginView,
    # ResetPasswordView,
    # ResetPasswordKeyView,
    PasswordChangeView,
    # AddEmailView,
)
# > Forms
from customer.forms import (
    # SignupForm,
    # LoginForm,
    # ResetPasswordForm,
    # ResetPasswordKeyForm,
    MyChangePasswordForm,
    # AddEmailForm,
    ProfileUpdateForm,
)


# class MySignupForm(SignupForm):
#     """
#     Django-allauth.

#     Creation de compte utilisateur.

#     """


# class MyLoginForm(LoginForm):
#     """
#     Django-allauth.

#     Connexion au compte utilisateur.

#     """


# class MyResetPasswordForm(ResetPasswordForm):
#     """
#     Django-allauth.

#     Reinitialisation mot de passe via mail

#     """


# class MyResetPasswordKeyForm(ResetPasswordKeyForm):
#     """
#     Django-allauth.

#     Reinitialisation du mot de passe via mail

#     """


class MyPasswordChangeView(LoginRequiredMixin, PasswordChangeView):
    """
    Django-allauth.

    Changement du mot de passe

    """

    form_class = MyChangePasswordForm
    template_name = 'pages/customer/password_change.html'
    success_url = reverse_lazy("customer:account_change_password")


# class MyAddEmailForm(AddEmailForm):
#     """
#     Django-allauth.

#     Changement d'e-mail

#     """


class ProfileUpdateView(LoginRequiredMixin, generic.FormView):
    """
    Account Settings.

    Edition du profil utilisateur
    """

    form_class = ProfileUpdateForm
    template_name = 'pages/customer/profile_update.html'
    success_url = reverse_lazy('customer:profile_update')

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
        messages.success(self.request, _("Votre profil est à jour"))
        return redirect(self.get_success_url())
