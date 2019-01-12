from django.conf.urls import url

from views import (
    index,
    article_detail,
    all_articles,
    all_categories,
    CategoryCreateView,
    category_detail,
    ArticleCreateView,
    )

urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^article/(?P<pk>[0-9]+)$', article_detail, name='article_detail'),
    url(r'^article/all$',all_articles,name='allarticles'),
    url(r'^category/all$',all_categories,name='allcategories'),
    url(r'^category/create$',CategoryCreateView.as_view(),name='category_create'),
    url(r'^category/(?P<pk>[0-9]+)$', category_detail, name='category_detail'),
    url(r'^article/create$', ArticleCreateView.as_view(), name='article_create'),
    ]