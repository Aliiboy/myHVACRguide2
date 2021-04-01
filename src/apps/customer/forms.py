"""
core forms.

Formulaires
"""

# > Django
from django.utils.translation import gettext_lazy as _
# > Forms django
from django.forms import ModelForm
# > Forms django-allauth
from allauth.account.forms import (
    SignupForm,
    LoginForm,
    ResetPasswordForm,
    ResetPasswordKeyForm,
    ChangePasswordForm,
    AddEmailForm,
)
# > Crispy Forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import (
        Layout,
        Fieldset,
        Row,
        Column,
        Field,
        Submit,
)
# > Django-recaptcha
from captcha.fields import ReCaptchaField
from captcha.widgets import ReCaptchaV2Checkbox
# > Settings
from myhvacrguide.settings import base as settings
# > Models
from customer.models import (
        CustomUser,
)


class MySignupForm(SignupForm):
    """
    Django-allauth.

    Creation de compte utilisateur.

    """

    captcha = ReCaptchaField(widget=ReCaptchaV2Checkbox)
    field_order = ['email', 'email2', 'password1', 'password2', 'captcha']

    def __init__(self, *args, **kwargs):
        super(MySignupForm, self).__init__(*args, **kwargs)
        # > Allauth : Email
        self.fields['email'].label = _('Adresse e-mail')
        self.fields['email'].widget.attrs.update(
            {
                # 'class': 'bg-dark',
                'placeholder': _('Entrez votre e-mail'),
            }
        )
        # > Allauth : Email de confirmation
        if settings.ACCOUNT_SIGNUP_EMAIL_ENTER_TWICE:
            self.fields['email2'].label = _('Confirmez votre adresse e-mail')
            self.fields['email2'].widget.attrs.update(
                {
                    # 'class': 'bg-dark',
                    'placeholder': _('Entrez votre e-mail'),
                }
            )

        # > Allauth : Mot de passe
        self.fields['password1'].label = _('Mot de passe')
        self.fields['password1'].widget.attrs.update(
            {
                # 'class': 'bg-dark',
                'placeholder': _('Entrez votre mot de passe'),
            }
        )
        # > Allauth : Mot de passe de confirmation
        if settings.ACCOUNT_SIGNUP_PASSWORD_ENTER_TWICE:
            self.fields['password2'].label = _('Confirmez votre mot de passe')
            self.fields['password2'].widget.attrs.update(
                {
                    # 'class': 'bg-dark',
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

    def __init__(self, *args, **kwargs):
        super(MyLoginForm, self).__init__(*args, **kwargs)
        # > Allauth : Email
        self.fields['login'].label = _('Adresse e-mail')
        self.fields['login'].widget.attrs.update(
            {
                # 'class': 'bg-dark',
                'placeholder': _('Entrez votre e-mail'),
            }
        )
        # > Allauth : Mot de passe
        self.fields['password'].label = _('Mot de passe')
        self.fields['password'].widget.attrs.update(
            {
                # 'class': 'bg-dark',
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
        # > Allauth : Se souvenir de moir
        self.fields['remember'].label = _('Se souvenir de moi')


class MyResetPasswordForm(ResetPasswordForm):
    """
    Django-allauth.

    Reinitialisation mot de passe via mail

    """

    def __init__(self, *args, **kwargs):
        super(MyResetPasswordForm, self).__init__(*args, **kwargs)
        # > Allauth : Email
        self.fields['email'].label = _('Adresse e-mail')
        self.fields['email'].widget.attrs.update(
            {
                # 'class': 'bg-dark',
                'placeholder': _('Entrez votre e-mail'),
            }
        )


class MyResetPasswordKeyForm(ResetPasswordKeyForm):
    """
    Django-allauth.

    Reinitialisation du mot de passe via mail

    """

    def __init__(self, *args, **kwargs):
        super(MyResetPasswordKeyForm, self).__init__(*args, **kwargs)
        # > Allauth : Mot de passe
        self.fields['password1'].label = _('Mot de passe')
        self.fields['password1'].widget.attrs.update(
            {
                # 'class': 'bg-dark',
                'placeholder': _('Entrez votre mot de passe'),
            }
        )
        # > Allauth : Mot de passe de confirmation
        self.fields['password2'].label = _('Confirmez votre mot de passe')
        self.fields['password2'].widget.attrs.update(
            {
                # 'class': 'bg-dark',
                'placeholder': _('Entrez votre mot de passe'),
            }
        )


class MyChangePasswordForm(ChangePasswordForm):
    """
    Django-allauth.

    Changement du mot de passe

    """

    def __init__(self, *args, **kwargs):
        super(MyChangePasswordForm, self).__init__(*args, **kwargs)
        # > Allauth : Mot de passe actuel
        self.fields['oldpassword'].label = _('Mot de passe actuel')
        self.fields['oldpassword'].widget.attrs.update(
            {
                # 'class': 'bg-dark',
                'placeholder': _('Entrez votre mot de passe'),
            }
        )
        # > Allauth : Mot de passe
        self.fields['password1'].label = _('Nouveau mot de passe')
        self.fields['password1'].widget.attrs.update(
            {
                # 'class': 'bg-dark',
                'placeholder': _('Nouveau votre mot de passe'),
            }
        )
        # > Allauth : Mot de passe de confirmation
        self.fields['password2'].label = _('Nouveau votre mot de passe')
        self.fields['password2'].widget.attrs.update(
            {
                # 'class': 'bg-dark',
                'placeholder': _('Nouveau votre mot de passe'),
            }
        )


class MyAddEmailForm(AddEmailForm):
    """
    Django-allauth.

    Changement d'e-mail

    """

    def __init__(self, *args, **kwargs):
        super(AddEmailForm, self).__init__(*args, **kwargs)
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
                    css_class='form-group mt-auto col-xl-4 col-lg-4 col-md-5 col-sm-5'),
                css_class='',
            ),

        )


class ProfileUpdateForm(ModelForm):
    """
    Profile Update.

    Edition du profil utilisateur
    """

    def __init__(self, user, *args, **kwargs):
        self.customuser = user
        kwargs['instance'] = user
        super(ProfileUpdateForm, self).__init__(*args, **kwargs)


    class Meta:
        model = CustomUser
        # exclude = ('user',)
        fields = ['last_name', 'first_name', ]
