"""
customer URL Configuration.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

# > Django
from django.urls import path
# > Vues
from customer.views import (
    MySignupView,
    MyLoginView,
    MyLogoutView,
    MyPasswordChangeView,
    MyAccountInactiveView,
    # ResetPasswordView,
    # ResetPasswordKeyView,
    # AddEmailView,
    ProfileUpdateView,
)


app_name = 'customer'
urlpatterns = [
    # > Django-allauth
    path("signup/", MySignupView.as_view(), name="account_signup"),
    path("login/", MyLoginView.as_view(), name="account_login"),
    path("logout/", MyLogoutView.as_view(), name="account_logout"),
    path('password/change/', MyPasswordChangeView.as_view(),
         name='account_change_password',
         ),
    # Si auth par social provider
    # path("password/set/", views.password_set, name="account_set_password"),
    path("inactive/", MyAccountInactiveView.as_view(),
         name="account_inactive",
         ),

    # E-mail
    # path("email/", views.email, name="account_email"),
    # path("confirm-email/", views.email_verification_sent,
    #      name="account_email_verification_sent"),
    # re_path(r"^confirm-email/(?P<key>[-:\w]+)/$", views.confirm_email,
    #         name="account_confirm_email"),

    # password reset
    # path("password/reset/", views.password_reset,
    #      name="account_reset_password"),
    # path("password/reset/done/", views.password_reset_done,
    #      name="account_reset_password_done"),
    # re_path(r"^password/reset/key/(?P<uidb36>[0-9A-Za-z]+)-(?P<key>.+)/$",
    #         views.password_reset_from_key,
    #         name="account_reset_password_from_key"),
    # path("password/reset/key/done/", views.password_reset_from_key_done,
    #      name="account_reset_password_from_key_done"),

    # > Profil
    path('profile/update/', ProfileUpdateView.as_view(),
         name='profile_update',
         ),
]
