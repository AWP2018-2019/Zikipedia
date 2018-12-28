from django.conf.urls import url

from views import (
    index,
    article_detail,
    )

urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^article/(?P<pk>[0-9]+)$', article_detail, name='article_detail'),
    ]