from django.urls import path
from .views import post_list, post_detail, create_post, edit_post, delete_post
app_name = 'blogapp'
urlpatterns = [
    path('', post_list,name='post_list'),
    path('create', create_post, name='create_post'),
    path('post/<slug>/edit/', edit_post, name='edit_post'),
    path('post/<slug>/', post_detail, name='post_detail'),
    path('post/<slug>/delete/', delete_post, name='delete_post'),
]