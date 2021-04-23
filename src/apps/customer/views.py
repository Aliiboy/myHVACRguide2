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
# > Django-allauth
from allauth.utils import (
    get_request_param,
)
from allauth.account.utils import (
    passthrough_next_redirect_url,
)
# > Django-allauth Views
from allauth.account.views import (
    CloseableSignupMixin,
    SignupView,
    LoginView,
    ConfirmEmailView,
    LogoutView,
    PasswordChangeView,
    PasswordResetView,
    PasswordResetDoneView,
    PasswordResetFromKeyView,
    PasswordResetFromKeyDoneView,
    AccountInactiveView,
    EmailVerificationSentView,
    # AddEmailView,
)
# > Forms
from customer.forms import (
    MySignupForm,
    MyLoginForm,
    MyChangePasswordForm,
    MyResetPasswordForm,
    MyResetPasswordKeyForm,
    # AddEmailForm,
    ProfileUpdateForm,
)
# > Settings
from myhvacrguide.settings import base as settings  # noqa


class MyCloseableSignupMixin(CloseableSignupMixin):
    template_name_signup_closed = (
        "pages/customer/signup_closed.html"
    )


class MySignupView(MyCloseableSignupMixin, SignupView):
    """
    Django-allauth.

    Creation de compte utilisateur.

    """

    template_name = 'pages/customer/signup.html'
    form_class = MySignupForm
    redirect_field_name = "next"
    success_url = None

    def get_context_data(self, **kwargs):  # noqa
        # Laisser SignupView et non MySignupView
        ret = super(SignupView, self).get_context_data(**kwargs)
        form = ret['form']
        email = self.request.session.get('account_verified_email')
        if email:
            email_keys = ['email']
            if settings.SIGNUP_EMAIL_ENTER_TWICE:
                email_keys.append('email2')
            for email_key in email_keys:
                form.fields[email_key].initial = email
        login_url = passthrough_next_redirect_url(self.request,
                                                  reverse("customer:account_login"),  # noqa
                                                  self.redirect_field_name)
        redirect_field_name = self.redirect_field_name
        redirect_field_value = get_request_param(self.request,
                                                 redirect_field_name)
        ret.update({"login_url": login_url,
                    "redirect_field_name": redirect_field_name,
                    "redirect_field_value": redirect_field_value})
        return ret


class MyConfirmEmailView(ConfirmEmailView):
    """
    Django-allauth.

    Envoie email de confirmation.

    """

    template_name = "pages/customer/email_confirm.html"


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


class MyPasswordResetView(PasswordResetView):
    """
    Django-allauth.

    Reinitialisation mot de passe via mail

    """

    template_name = "pages/customer/password_reset.html"
    form_class = MyResetPasswordForm
    success_url = reverse_lazy("customer:account_reset_password_done")
    redirect_field_name = "next"

    def get_context_data(self, **kwargs):  # noqa
        # Laisser PasswordResetView et non MyPasswordResetView
        ret = super(PasswordResetView, self).get_context_data(**kwargs)  # noqa
        login_url = passthrough_next_redirect_url(self.request,
                                                  reverse("customer:account_login"),  # noqa
                                                  self.redirect_field_name)
        # NOTE: For backwards compatibility
        ret['password_reset_form'] = ret.get('form')
        # (end NOTE)
        ret.update({"login_url": login_url})
        return ret


class MyPasswordResetDoneView(PasswordResetDoneView):
    """
    Django-allauth.

    Envoie du mail de reinitialisation

    """

    template_name = (
        "pages/customer/password_reset_done.html"
    )


class MyPasswordResetFromKeyView(PasswordResetFromKeyView):
    """
    Django-allauth.

    Nouveau mot de passe

    """

    template_name = "pages/customer/password_reset_from_key.html"
    form_class = MyResetPasswordKeyForm
    success_url = reverse_lazy("customer:account_reset_password_from_key_done")

    def get_context_data(self, **kwargs):  # noqa
        # Laisser PasswordResetDoneView et non MyPasswordResetFromKeyView
        ret = super(PasswordResetFromKeyView, self).get_context_data(**kwargs)  # noqa
        ret['action_url'] = reverse(
            'customer:account_reset_password_from_key',
            kwargs={'uidb36': self.kwargs['uidb36'],
                    'key': self.kwargs['key']})
        return ret


class MyPasswordResetFromKeyDoneView(PasswordResetFromKeyDoneView):
    """
    Django-allauth.

    Mot de passe modifié

    """

    template_name = "pages/customer/password_reset_from_key_done.html"


class MyAccountInactiveView(AccountInactiveView):
    """
    Django-allauth.

    Lorsque que le compte est inactif

    """

    template_name = 'pages/customer/account_inactive.html'


class MyEmailVerificationSentView(EmailVerificationSentView):
    """
    Django-allauth.

    Lorque l'email de confirmation est envoye

    """

    template_name = (
        'pages/customer/verification_sent.html')


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
        messages.info(self.request, _("Votre profil est à jour"))
        return redirect(self.get_success_url())


# class MyAddEmailForm(AddEmailForm):
#     """
#     Django-allauth.

#     Changement d'e-mail

#     """
