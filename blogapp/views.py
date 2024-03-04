from django.shortcuts import get_object_or_404, redirect, render
from django.core.paginator import Paginator
from django.urls import reverse
from .models import Post
from .forms import PostForm

def post_list(request):
    #posts = Post.objects.filter(status__in=[1,2])
    posts = Post.objects.filter(status=2)
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

def create_post(request):
    title = "Create"
    form = PostForm(request.POST or None, request.FILES or None)
    if request.method == 'POST':
        if form.is_valid():
            form.instance.created_by = request.user
            form.save()
            return redirect(reverse("blogapp:post_detail", kwargs={
                'slug':form.instance.slug,
                }))

    context = {
        'title': title,
        'form': form,
    }
    return render(request, 'create_post.html', context)

def edit_post(request, slug):
    title = "Edit"
    post = get_object_or_404(Post, slug=slug)
    form = PostForm(request.POST or None,
                     request.FILES or None,
                       instance=post)
    
    if request.method == 'POST':
        if form.is_valid():
            form.instance.created_by = request.user
            form.save()
            return redirect(reverse("blogapp:post_detail", kwargs={
                'slug':form.instance.slug,
                }))

    context = {
        'title': title,
        'form': form,
    }

    return render(request, 'create_post.html', context)

def delete_post(request, slug):
    post = get_object_or_404(Post, slug=slug)
    post.delete()
    return redirect(reverse('blogapp:post_list'))