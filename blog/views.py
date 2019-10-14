from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from .models import Blog
from .forms import BlogForm

from django.views.generic import(
    CreateView,
    ListView,
    UpdateView,
    DeleteView,
    DetailView
)


class BlogObjectMixin(object):
    model = Blog
    
    def get_object(self):
        id_ = self.kwargs.get("id")
        if id is not None:
            return get_object_or_404(self.model , id = id_)

class BlogCreateView(CreateView):
    template_name = 'create_blog.html'
    form_class = BlogForm
    queryset = Blog.objects.all() 
    success_url = '../'

    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)

class BlogView(ListView):
    template_name = 'blog_list.html'
    queryset = Blog.objects.all()

class BlogDetailView(BlogObjectMixin,DetailView):
    template_name = 'detail_blog.html'


class BlogUpdateView(BlogObjectMixin, UpdateView):
    template_name = 'create_blog.html'
    form_class = BlogForm

    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)

class BlogDeleteView(BlogObjectMixin,DeleteView):
    template_name = 'delete_blog.html'

    def get_success_url(self):
        return reverse("blog:blog-list")    