"""
core forms.

Formulaires
"""

# > Django
from django.contrib.sites.shortcuts import get_current_site
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
# > Forms django
from django.forms import ModelForm
# > Forms django-allauth
from allauth.utils import (
    build_absolute_uri,
)
from allauth.account.utils import (
    user_pk_to_url_str,
    user_username,
)
from allauth.account.app_settings import (
    AUTHENTICATION_METHOD,
    AuthenticationMethod,
)
from allauth.account.adapter import get_adapter
from allauth.account.forms import (
    SignupForm,
    LoginForm,
    ChangePasswordForm,
    ResetPasswordForm,
    ResetPasswordKeyForm,
    AddEmailForm,
    default_token_generator,
)
# > Crispy Forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import (
        Layout,
        Row,
        Column,
        Submit,
)
# > Django-recaptcha
from captcha.fields import ReCaptchaField
from captcha.widgets import ReCaptchaV2Checkbox
# > Models
from customer.models import (
        CustomUser,
)
# > Settings
from myhvacrguide.settings import base as settings  # noqa


class MySignupForm(SignupForm):
    """
    Django-allauth.

    Creation de compte utilisateur.

    """

    captcha = ReCaptchaField(widget=ReCaptchaV2Checkbox)
    field_order = ['email', 'email2', 'password1', 'password2', 'captcha']

    def __init__(self, *args, **kwargs):  # noqa
        # > Django : Supprimer le suffix ":" des label
        kwargs.setdefault('label_suffix', '')
        super(MySignupForm, self).__init__(*args, **kwargs)
        # > Allauth : Email
        self.fields['email'].label = _('Adresse e-mail')
        self.fields['email'].widget.attrs.update(
            {
                'class': 'form-control',
                'placeholder': _('Entrez votre e-mail'),
            }
        )
        # > Allauth : Email de confirmation
        if settings.ACCOUNT_SIGNUP_EMAIL_ENTER_TWICE:
            self.fields['email2'].label = _('Confirmez votre adresse e-mail')
            self.fields['email2'].widget.attrs.update(
                {
                    'class': 'form-control',
                    'placeholder': _('Entrez votre e-mail'),
                }
            )

        # > Allauth : Mot de passe
        self.fields['password1'].label = _('Mot de passe')
        self.fields['password1'].widget.attrs.update(
            {
                'class': 'form-control',
                'placeholder': _('Entrez votre mot de passe'),
            }
        )
        # > Allauth : Mot de passe de confirmation
        if settings.ACCOUNT_SIGNUP_PASSWORD_ENTER_TWICE:
            self.fields['password2'].label = _('Confirmez votre mot de passe')
            self.fields['password2'].widget.attrs.update(
                {
                    'class': 'form-control',
                    'placeholder': _('Entrez votre mot de passe'),
                }
            )
        # > Recaptcha
        self.fields['captcha'].widget.attrs.update(
            {
                'data-callback': 'enableSubmitBtn',
                'data-theme': 'light',
                'data-size': 'normal',
            }
        )


class MyLoginForm(LoginForm):
    """
    Django-allauth.

    Connexion au compte utilisateur.

    """

    captcha = ReCaptchaField(widget=ReCaptchaV2Checkbox)

    def __init__(self, *args, **kwargs):  # noqa
        # > Django : Supprimer le suffix ":" des label
        kwargs.setdefault('label_suffix', '')
        super(MyLoginForm, self).__init__(*args, **kwargs)
        # > Allauth : Email
        self.fields['login'].label = _('Adresse e-mail')
        self.fields['login'].widget.attrs.update(
            {
                'class': 'form-control',
                'placeholder': _('Entrez votre e-mail'),
            }
        )
        # > Allauth : Mot de passe
        self.fields['password'].label = _('Mot de passe')
        self.fields['password'].widget.attrs.update(
            {
                'class': 'form-control',
                'placeholder': _('Entrez votre mot de passe'),
            }
        )
        # > Recaptcha
        self.fields['captcha'].widget.attrs.update(
            {
                'data-callback': 'enableSubmitBtn',
                # 'data-theme': 'light',
                'data-size': 'normal',
            }
        )
        # > Allauth : Se souvenir de moir
        self.fields['remember'].label = _('Se souvenir de moi')
        self.fields['remember'].widget.attrs.update(
            {
                'class': 'form-check-input',
            }
        )


class MyChangePasswordForm(ChangePasswordForm):
    """
    Django-allauth.

    Changement du mot de passe

    """

    def __init__(self, *args, **kwargs):  # noqa
        # > Django : Supprimer le suffix ":" des label
        kwargs.setdefault('label_suffix', '')
        super(MyChangePasswordForm, self).__init__(*args, **kwargs)
        # > Allauth : Mot de passe actuel
        self.fields['oldpassword'].label = _('Mot de passe actuel')
        self.fields['oldpassword'].widget.attrs.update(
            {
                'class': 'form-control',
                'placeholder': _('Entrez votre mot de passe'),
            }
        )
        # > Allauth : Mot de passe
        self.fields['password1'].label = _('Nouveau mot de passe')
        self.fields['password1'].widget.attrs.update(
            {
                'class': 'form-control',
                'placeholder': _('Nouveau votre mot de passe'),
            }
        )
        # > Allauth : Mot de passe de confirmation
        self.fields['password2'].label = _('Nouveau votre mot de passe')
        self.fields['password2'].widget.attrs.update(
            {
                'class': 'form-control',
                'placeholder': _('Nouveau votre mot de passe'),
            }
        )


class MyResetPasswordForm(ResetPasswordForm):
    """
    Django-allauth.

    Reinitialisation mot de passe via mail

    """

    def __init__(self, *args, **kwargs):  # noqa
        # > Django : Supprimer le suffix ":" des label
        kwargs.setdefault('label_suffix', '')
        super(MyResetPasswordForm, self).__init__(*args, **kwargs)
        # > Allauth : Email
        self.fields['email'].label = _('Adresse e-mail')
        self.fields['email'].widget.attrs.update(
            {
                'class': 'form-control',
                'placeholder': _('Entrez votre e-mail'),
            }
        )

    def save(self, request, **kwargs):
        current_site = get_current_site(request)
        email = self.cleaned_data["email"]
        token_generator = kwargs.get("token_generator",
                                     default_token_generator)

        for user in self.users:

            temp_key = token_generator.make_token(user)

            # save it to the password reset model
            # password_reset = PasswordReset(user=user, temp_key=temp_key)
            # password_reset.save()

            # send the password reset email
            path = reverse("customer:account_reset_password_from_key",
                           kwargs=dict(uidb36=user_pk_to_url_str(user),
                                       key=temp_key))
            url = build_absolute_uri(
                request, path)

            context = {"current_site": current_site,
                       "user": user,
                       "password_reset_url": url,
                       "request": request}

            if AUTHENTICATION_METHOD \
                    != AuthenticationMethod.EMAIL:
                context['username'] = user_username(user)
            get_adapter(request).send_mail(
                'account/email/password_reset_key',
                email,
                context)
        return self.cleaned_data["email"]


class MyResetPasswordKeyForm(ResetPasswordKeyForm):
    """
    Django-allauth.

    Reinitialisation du mot de passe via mail

    """

    def __init__(self, *args, **kwargs):  # noqa
        # > Django : Supprimer le suffix ":" des label
        kwargs.setdefault('label_suffix', '')
        super(MyResetPasswordKeyForm, self).__init__(*args, **kwargs)
        # > Allauth : Mot de passe
        self.fields['password1'].label = _('Mot de passe')
        self.fields['password1'].widget.attrs.update(
            {
                'class': 'form-control',
                'placeholder': _('Entrez votre mot de passe'),
            }
        )
        # > Allauth : Mot de passe de confirmation
        self.fields['password2'].label = _('Confirmez votre mot de passe')
        self.fields['password2'].widget.attrs.update(
            {
                'class': 'form-control',
                'placeholder': _('Entrez votre mot de passe'),
            }
        )


class MyAddEmailForm(AddEmailForm):
    """
    Django-allauth.

    Changement d'e-mail

    """

    def __init__(self, *args, **kwargs):  # noqa
        # > Django : Supprimer le suffix ":" des label
        kwargs.setdefault('label_suffix', '')
        super(MyAddEmailForm, self).__init__(*args, **kwargs)
        # > Allauth : Email
        self.fields['email'].label = _('Ajouter une adresse e-mail')
        self.fields['email'].widget.attrs.update(
            {
                # 'class': 'bg-dark',
                'placeholder': _('Adresse e-mail'),
            }
        )

        # > Crispy forms
        self.helper = FormHelper()
        # Attributs
        # self.helper.form_id = ''
        self.helper.form_class = 'px-3'
        self.helper.form_method = 'post'
        # self.helper.form_action = ''
        # > Layout
        self.helper.layout = Layout(
            Row(
                # > Remplacer Field par Column si utilisation de Row
                Column('email',
                       css_class='col-xl-8 col-lg-8 col-md-7 col-sm-7'),
                Column(
                    Submit('action_add',
                           _('Ajouter un e-mail'),
                           css_class='btn btn-success'),
                    css_class='form-group mt-auto col-xl-4 col-lg-4 col-md-5 col-sm-5'),  # noqa
                css_class='',
            ),

        )


class ProfileUpdateForm(ModelForm):
    """
    Profile Update.

    Edition du profil utilisateur
    """

    def __init__(self, user, *args, **kwargs):  # noqa
        # > Django : Supprimer le suffix ":" des label
        kwargs.setdefault('label_suffix', '')
        self.customuser = user
        kwargs['instance'] = user
        super(ProfileUpdateForm, self).__init__(*args, **kwargs)
        # > Nom
        self.fields['last_name'].label = _('Nom')
        self.fields['last_name'].widget.attrs.update(
            {
                'class': 'form-control',
                'placeholder': _('Entrez votre nom'),
            }
        )
        # > Prenom
        self.fields['first_name'].label = _('Prenom')
        self.fields['first_name'].widget.attrs.update(
            {
                'class': 'form-control',
                'placeholder': _('Entrez votre prenom'),
            }
        )

    class Meta:  # noqa
        model = CustomUser
        # exclude = ('user',)
        fields = ['last_name', 'first_name', ]
