from django.conf.urls import url
from . import views
from . import views_cbv

app_name = 'blog'

urlpatterns = [
    url(r'^new$', views.post_new, name='post_new'),

    url(r'^$', views_cbv.post_list, name='post_list'),
    url(r'^detail/(?P<pk>\d+)/$', views_cbv.post_detail, name='post_detail'),
    url(r'^new/$', views_cbv.post_new, name='post_new'),
    url(r'^detail/(?P<pk>\d+)/edit/$', views_cbv.post_edit, name='post_edit'),
    url(r'^detail/(?P<pk>\d+)/delete/$', views_cbv.post_delete, name='post_delete'),
]