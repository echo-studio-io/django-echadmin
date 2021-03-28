from django.urls import path
from . import auth_urls

from .views import CenterView

app_name = 'account'
urlpatterns = [
    path('', CenterView.as_view(), name='center'),
] + auth_urls.urlpatterns
