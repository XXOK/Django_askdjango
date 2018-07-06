from django.conf.urls import url
from . import views, views_cbv

app_name = 'dojo'

urlpatterns = [
    url(r'^post_new', views.post_new, name='post_new'),
    url(r'^(?P<pk>\d+)/edit', views.post_edit),

    url(r'^create_user$', views.create_user, name='create_user'),

    url(r'^sum/(?P<numbers>[\d/]+)/$', views.mysum),
    url(r'^hello/(?P<name>[ㄱ-힣]+)/(?P<age>\d+)/$', views.profile),

    url(r'^post_list1$',views.post_list1),
    url(r'^post_list2$',views.post_list2),
    url(r'^post_list3$',views.post_list3),
    url(r'^excel_download$',views.excel_download),

    url(r'^cbv/post_list1$',views_cbv.post_list1),
    url(r'^cbv/post_list2$',views_cbv.post_list2),
    # url(r'^cbv/post_list3$',views_cbv.post_list3),
    # url(r'^cbv/excel_download$',views_cbv.excel_download),

    url(r'^(?P<pk>[\d/]+)/$',views.post_detail, name='post_detail'),
]