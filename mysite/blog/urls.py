from django.urls import path
from . import views

urlpatterns = [
    # post view
    path(r'', views.post_list, name='post_list'),
    # url(r'^(?P<year>\d{4})/(?P<month>\d{2})/(?P<day>\d{2})/'\r'(?P<post>[-\w]+)/$',
    path(r'^(<int:year>)/(<int:month>)/(<int:day>)/(?P<post>[-\w]+)/$', views.post_detail, name='post_detail'),
]
