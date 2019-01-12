from django.conf.urls import url

from views import (
    index,
    article_detail,
    all_articles,
    all_categories,
    CategoryCreateView,
    )

urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^article/(?P<pk>[0-9]+)$', article_detail, name='article_detail'),
    url(r'^article/all$',all_articles,name='allarticles'),
    url(r'^category/all$',all_categories,name='allcategories'),
    url(r'^category/create$',CategoryCreateView.as_view(),name='category_create'),
    ]