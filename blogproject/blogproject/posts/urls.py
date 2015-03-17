from django.conf.urls import patterns, url

from .views import PostList, PostDetail, \
    PostCreate, PostUpdate, PostDelete, \
    CategoryList, CategoryDetail

urlpatterns = patterns('',

    # example.com/blog/
    url(r'^$', PostList.as_view(), name='blog'),

    # example.com/blog/1
    url(r'^(?P<page>\d+)/$', PostList.as_view(), name='post_list'),

    # example.com/blog/post/1
    url(r'^post/(?P<pk>\d+)/$', PostDetail.as_view(), name='post_detail'),

    # example.com/blog/post/1/update
    url(r'^post/(?P<pk>\d+)/update/$', PostUpdate.as_view(), name='post_update'),

    # example.com/blog/post/1/delete
    url(r'^post/(?P<pk>\d+)/delete/$', PostDelete.as_view(), name='post_delete'),

    # example.com/blog/posts/add
    url(r'^posts/add/$', PostCreate.as_view(), name='post_create'),

    # example.com/blog/categories
    url(r'^categories$', CategoryList.as_view(), name='category_list'),

    # example.com/blog/category/1
    url(r'^category/(?P<pk>\d+)/$', CategoryDetail.as_view(), name='category_detail'),
)
