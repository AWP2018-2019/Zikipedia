from django.conf.urls import url

from views import (
    index,
    article_detail,
    all_articles,
    all_categories,
    CategoryCreateView,
    category_detail,
    ArticleCreateView,
    ArticleEditView,
    CategoryEditView,
    ArticleDeleteView,
    CategoryDeleteView,
    RegisterView,
    LoginView,
    logout_view,
    )

urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^article/(?P<pk>[0-9]+)$', article_detail, name='article_detail'),
    url(r'^article/all$',all_articles,name='allarticles'),
    url(r'^category/all$',all_categories,name='allcategories'),
    url(r'^category/create$',CategoryCreateView.as_view(),name='category_create'),
    url(r'^category/(?P<pk>[0-9]+)$', category_detail, name='category_detail'),
    url(r'^article/create$', ArticleCreateView.as_view(), name='article_create'),
    url(r'^article/edit/(?P<pk>[0-9]+)$', ArticleEditView.as_view(), name='article_edit'),
    url(r'^category/edit/(?P<pk>[0-9]+)$', CategoryEditView.as_view(), name='category_edit'),
    url(r'^article/delete/(?P<pk>[0-9]+)$', ArticleDeleteView.as_view(), name='article_delete'),
    url(r'^category/delete/(?P<pk>[0-9]+)$', CategoryDeleteView.as_view(), name='category_delete'),
    url(r'^register/$', RegisterView.as_view(), name='register'),
    url(r'^login/$', LoginView.as_view(), name='login'),
    url(r'^logout/$', logout_view, name='logout'),
    ]