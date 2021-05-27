"""
core URL Configuration.

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
from django.urls import path, reverse_lazy
# > Vues
from django.views.generic.base import RedirectView
from core.views import (
    IndexUiView,
)


app_name = 'core'
urlpatterns = [
    # > Pages publiques
    path('', RedirectView.as_view(
        url=reverse_lazy('core:ui_home')),
         name='index',
         ),
    # > UI
    path('home/', IndexUiView.as_view(), name='ui_home'),
]
