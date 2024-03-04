from typing import Any
from django.db.models.base import Model as Model
from django.db.models.query import QuerySet
from django.forms import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.core.paginator import Paginator
from django.urls import reverse, reverse_lazy
from .models import Post
from .forms import PostForm
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

#class views
class PostListView(ListView):
    model = Post
    template_name = 'blog/post_list.html'
    paginate_by = 10


    def get_queryset(self) -> QuerySet[Any]:
        return Post.objects.filter(status=2)
    
class PostDetailView(DetailView):
    model = Post
    
    slug_field = 'slug'
    #slug_url_kwarg = 'get_slug'
    template_name = 'blog/post.html'

class PostCreateView(CreateView):
    model = Post
    template_name = 'blog/create_post.html'
    form_class = PostForm

    def get_context_data(self, **kwargs: Any):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Create'
        return context
    
    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        form.instance.author = self.request.user
        form.save()
        return redirect(reverse('blogapp:blog_post_detail',kwargs={'slug':form.instance.slug}))
    
class PostUpdateView(UpdateView):
    model = Post
    template_name = 'blog/create_post.html'
    form_class = PostForm

    def get_context_data(self, **kwargs: Any):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Edit'
        return context
    
    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        form.instance.author = self.request.user
        form.save()
        return redirect(reverse('blogapp:blog_post_detail',kwargs={'slug':form.instance.slug}))


class PostDeleteView(DeleteView):
    model = Post
    template_name = 'blog/delete_post.html'
    def get_object(self) -> Model:
        slug = self.kwargs.get('slug')
        return get_object_or_404(Post, slug=slug)
    
    def get_success_url(self):
        return reverse_lazy('blogapp:blog_post_list')



#function views
def post_list(request):
    #posts = Post.objects.filter(status__in=[1,2])
    posts = Post.objects.filter(status=2)
    paginator = Paginator(posts, 2)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'page_obj':page_obj,

       }
    return render(request,'post_list.html',context)

def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug)
    #post = Post.objects.get(slug=slug)
    context = {'object':post,}
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

