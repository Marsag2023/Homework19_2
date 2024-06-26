from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, DetailView, ListView, UpdateView, DeleteView
from pytils.translit import slugify

from blogpost.forms import BlogPostForm
from blogpost.models import BlogPost


class BlogPostCreateView(LoginRequiredMixin, CreateView):
    model = BlogPost
    form_class = BlogPostForm
    success_url = reverse_lazy('blogpost:list')

    def form_valid(self, form):
        if form.is_valid():
            new_blog = form.save()
            new_blog.slug = slugify(new_blog.title)
            new_blog.save()
        return super().form_valid(form)

    def get_form_class(self):
        user = self.request.user
        if user.has_perm('blogpost.add_blogpost'):
            return BlogPostForm
        raise PermissionDenied



class BlogPostListView(LoginRequiredMixin, ListView):
    model = BlogPost
    login_url = "/users/login/"
    redirect_field_name = "login"


    def get_queryset(self, *args, **kwargs):
        queryset = super().get_queryset(*args, **kwargs)
        queryset = queryset.filter(is_active=True)
        return queryset


class BlogPostDetailView(LoginRequiredMixin, DetailView):
    model = BlogPost

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.number_of_views += 1
        self.object.save()
        return self.object


class BlogPostUpdateView(LoginRequiredMixin, UpdateView):
    model = BlogPost
    form_class = BlogPostForm

    def form_valid(self, form):
        if form.is_valid():
            new_blog = form.save()
            new_blog.slug = slugify(new_blog.title)
            new_blog.save()
        return super().form_valid(form)

    def get_form_class(self):
        user = self.request.user
        if user.has_perm('blogpost.change_blogpost'):
            return BlogPostForm
        raise PermissionDenied

    def get_success_url(self):
        return reverse('blogpost:view', args=[self.kwargs.get('pk')])




class BlogPostDeleteView(LoginRequiredMixin, DeleteView):
    model = BlogPost
    success_url = reverse_lazy('blogpost:list')

    def get_form_class(self):
        user = self.request.user
        if user.has_perm('blogpost.delete_blogpost'):
            return BlogPostForm
        raise PermissionDenied







def toggle_activity(request, pk):
    blogpost_item = get_object_or_404(BlogPost, pk=pk)
    if blogpost_item.is_active:
        blogpost_item.is_active = False
    else:
        blogpost_item.is_active = True
    blogpost_item.save()
    return redirect(reverse('blogpost:list'))

