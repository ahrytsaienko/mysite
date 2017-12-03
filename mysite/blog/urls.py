from django.urls import path
from . import views

urlpatterns = [
    # post view
    path(r'', views.PostListView.as_view(), name='post_list'),
    # url(r'^(?P<year>\d{4})/(?P<month>\d{2})/(?P<day>\d{2})/'\r'(?P<post>[-\w]+)/$',
    path(r'<int:year>/<int:month>/<int:day>/<post>/', views.post_detail, name='post_detail'),
]
