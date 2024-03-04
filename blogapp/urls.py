from django.urls import path
from .views import (
    post_list,
    post_detail,
    create_post, 
    edit_post, 
    delete_post,

    PostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView
)


app_name = 'blogapp'
urlpatterns = [
    path('', post_list,name='post_list'),
    path('create', create_post, name='create_post'),
    path('post/<slug>/', post_detail, name='post_detail'),
    path('post/<slug>/edit/', edit_post, name='edit_post'),
    path('post/<slug>/delete/', delete_post, name='delete_post'),


    path('blog/', PostListView.as_view(), name='blog_post_list'),
    path('blog/<slug>/', PostDetailView.as_view(), name='blog_post_detail' ),
    path('blog/create', PostCreateView.as_view(), name='blog_create_post'),
    path('blog/<slug>/edit/', PostUpdateView.as_view(), name='blog_edit_post'),
    path('blog/<slug>/delete/', PostDeleteView.as_view(), name='blog_delete_post')
]