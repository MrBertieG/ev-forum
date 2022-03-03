import random
import string
from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views import generic, View
from django.contrib import messages
from .models import Post, Category
from .forms import CommentForm
from django.http import HttpResponseRedirect

class CategoryList(generic.ListView):
    """View to render the category list"""
    model = Category
    template_name = 'index.html'
    paginate_by = 6

    def get_context_data(self, **kwargs):
        context = super(CategoryList, self).get_context_data(**kwargs)
        context['post'] = Post.objects.order_by('-created')
        return context


class CategoryDetail(View):
    """View to render details for a chosen category"""
    def get(self, request, name, *args, **kwargs):
        queryset = Category.objects
        category = get_object_or_404(queryset, name=name)
        posts = category.category_posts.order_by('created')

        return render(
            request,
            'category_detail.html',
            {
                "category": category,
                "posts": posts
            },
        )


@method_decorator(login_required, name='post')
class PostDetails(View):
    """View to render details for a chosen post"""
    def get(self, request, id, *args, **kwargs):
        queryset = Post.objects
        post = get_object_or_404(queryset, id=id)
        comments = post.post_comments.order_by('created')
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True
        
        return render(
            request,
            'post_detail.html',
            {
                "post": post,
                "comments": comments,
                "liked": liked,
                "comment_form": CommentForm()
            },
        )

    def post(self, request, id, *args, **kwargs):
        queryset = Post.objects
        post = get_object_or_404(queryset, id=id)
        comments = post.post_comments.order_by('created')
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True
        comment_form = CommentForm(data=request.POST)

        if comment_form.is_valid():
            comment_form.instance.author = request.user
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.save()
            messages.add_message(request, messages.SUCCESS, 
                                'Commented successfully')
        else:
            comment_form = CommentForm()
        
        return render(
            request,
            'post_detil.html',
            {
                "post": post,
                "comments": comments,
                "liked": liked,
                "comment_form": CommentForm()
            },
        )


class ContactUs(View):
    """Render view to allow users to send a message to admin"""
    def get(self, request, *args, **kwargs):

        return render(
            request,
            'contact_us.html',
            {
                'contact_us_form': ContactForm()
            },
        )