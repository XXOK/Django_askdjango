from django.conf.urls import url
from . import views, views_cbv

app_name = 'blog'

urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),
    url(r'^detail/(?P<id>\d+)/$', views.post_detail, name='post_detail'),
    url(r'^cbv/new/', views_cbv.post_new),
]