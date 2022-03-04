import random
import string
from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views import generic, View
from django.contrib import messages
from .models import Post, Category
from .forms import PostAddForm, CommentForm, ContactForm
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
class PostDetail(View):
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


@method_decorator(login_required, name='post')
class PostAdd(View):
    """View to allow adding of new posts"""
    def get(self, request, *args, **kwargs):
        model = Post
        template_name = 'add_post.html'

        return render(
            request,
            'add_post.html',
            {
                'post_add_form': PostAddForm()
            },
        )
    
    def post(self, request, *args, **kwargs):
        letterstr = string.ascii_lowercase
        slugval = ''.join(random.choice(letterstr)for i in range(6))

        post_add_form = PostAddForm(data=request.POST)

        if post_add_form.is_valid():
            post = post_add_form.save(commit=False)
            post.author = request.user
            post.slug = slugval
            if len(request.FILES) !=0:
                post.image = request.FILES['image']

            post.save()
            messages.add_message(request, messages.SUCCESS,
                                    'Post successfully added!')
        else:
            messages.add_message(request, messages.WARNING,
                                    'Failed to add post' +
                                    'See guidance on creating a post!')
        
        return redirect(reverse('post_detail', args=[post.id]))


@method_decorator(login_required, name='post')
class PostEdit(View):
    """ View to allow ediiting of existing posts"""
    def get(self, request, od, *args, **kwargs):
        queryset = Post.objects
        post = get_object_or_404(queryset, id=id)
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True

        return render (
            request,
            'edit_post.html',
            {
                'liked': liked,
                'post_edit_form': PostAddForm(instance=post)
            },
        )

    def post(self, request, id, *args, **kwargs):
        queryset = Post.objects
        comments = post.post_comments.order_by('created')
        liked = False

        post_edit_form = PostAddForm(request,POST, instance=post)

        if request.user == post.author:
            if post_edit_form.is_valid():
                post_edit_form.save()
                messages.add_message(request, messages.SUCCESS,
                        'Post successfully amended!')
            if post.likes.filter(id=self.request.user.id).exists():
                liked = True
            else:
                post_edit_form = PostAddForm(instance=post)
                messages.add_message(request, messages.WARNING,
                                    'Failed to add post' +
                                    'See guidance on creating a post!')
            
            return render(
                request, 'post_detail.html',
                {
                    "post": post,
                    "comments": comments,
                    "liked": liked,
                    "comment_form": CommentForm()
                },
            )


@method_decorator(login_required, name='post')
class PostLike(View):
    """Renders likes under the post"""
    def post(self, request, slug, *args, **kwargs):
        post = get_object_or_404(Post, slug=slug)
        if post.likes.filter(id=request.user.id).exists():
            post.likes.remove(request.user)
        else:
            post.likes.add(request.user)

        return redirect(reverse('post_detail', args=[post.id]))


@login_required
def delete_post(request, id, *args, **kwargs):
    """ View to delete post """
    queryset = Post.objects
    post = get_object_or_404(queryset, id=id)

    if request.user == post.author:
        post.delete()
        messages.add_message(request, messages.SUCCESS,
                             'Post deleted!')

    return redirect('home')


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