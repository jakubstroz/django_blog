from django.shortcuts import get_object_or_404, render
from .models import Post

def post_list(request):
    posts = Post.objects.filter(status=2)

    context = {'object_list':posts,}
    return render(request,'post_list.html',context)

def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug)
    #post = Post.objects.get(slug=slug)
    context = {'post_detail':post,}
    return render(request,'post.html',context)