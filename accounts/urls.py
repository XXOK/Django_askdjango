from django.conf.urls import url
from . import views

app_name = 'accounts'

urlpatterns = [
    url(r'^profile/$', views.profile),
    url(r'^signup/$', views.signup, name='signup'),
]