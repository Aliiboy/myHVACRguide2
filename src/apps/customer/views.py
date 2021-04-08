"""
customer views.

Vues
"""

# > Django
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.sites.shortcuts import get_current_site
from django.shortcuts import redirect
from django.urls import reverse, reverse_lazy
from django.utils.translation import gettext_lazy as _
from django.views import generic
# > Django-allauth Utils
from allauth.utils import (
    get_request_param,
)
from allauth.account.utils import (
    passthrough_next_redirect_url,
)
# > Django-allauth Views
from allauth.account.views import (
    SignupView,
    LoginView,
    LogoutView,
    PasswordChangeView,
    AccountInactiveView,
    # ResetPasswordView,
    # ResetPasswordKeyView,
    # AddEmailView,
)
# > Forms
from customer.forms import (
    MySignupForm,
    MyLoginForm,
    MyChangePasswordForm,
    # ResetPasswordForm,
    # ResetPasswordKeyForm,
    # AddEmailForm,
    ProfileUpdateForm,
)


class MySignupView(SignupView):
    """
    Django-allauth.

    Creation de compte utilisateur.

    """

    template_name = 'pages/customer/login.html'
    form_class = MySignupForm
    redirect_field_name = "next"
    success_url = None


class MyLoginView(LoginView):
    """
    Django-allauth.

    Connexion au compte utilisateur.

    """

    form_class = MyLoginForm
    template_name = 'pages/customer/login.html'
    success_url = None
    redirect_field_name = "next"

    def get_context_data(self, **kwargs):  # noqa
        # Laisser LoginView et non MyLoginView
        ret = super(LoginView, self).get_context_data(**kwargs)  # noqa
        signup_url = passthrough_next_redirect_url(self.request,
                                                   reverse("customer:account_signup"),  # noqa
                                                   self.redirect_field_name)
        redirect_field_value = get_request_param(self.request,
                                                 self.redirect_field_name)
        site = get_current_site(self.request)

        ret.update({"signup_url": signup_url,
                    "site": site,
                    "redirect_field_name": self.redirect_field_name,
                    "redirect_field_value": redirect_field_value})
        return ret


class MyLogoutView(LogoutView):
    """
    Django-allauth.

    Se deconnecter du compte utilisateur.

    """

    template_name = 'pages/customer/logout.html'
    redirect_field_name = "next"


class MyPasswordChangeView(LoginRequiredMixin, PasswordChangeView):
    """
    Django-allauth.

    Changement du mot de passe

    """

    form_class = MyChangePasswordForm
    template_name = 'pages/customer/password_change.html'
    success_url = reverse_lazy("customer:account_change_password")


class MyAccountInactiveView(AccountInactiveView):
    """
    Django-allauth.

    Lorsque que le compte est inactif

    """

    template_name = 'pages/customer/account_inactive.html'


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
