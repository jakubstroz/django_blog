from django.shortcuts import get_object_or_404, render
from django.core.paginator import Paginator
from .models import Post

def post_list(request):
    posts = Post.objects.filter(status__in=[1,2])
    paginator = Paginator(posts, 2)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'object_list':page_obj,

        }
    return render(request,'post_list.html',context)

def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug)
    #post = Post.objects.get(slug=slug)
    context = {'post_detail':post,}
    return render(request,'post.html',context)