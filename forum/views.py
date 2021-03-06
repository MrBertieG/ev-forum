import random
import string
from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views import generic, View
from django.contrib import messages
from .models import Post, Category, Comment
from .forms import PostAddForm, CommentForm, ContactForm, PostEditForm
from django.http import HttpResponseRedirect

# Views for PostDetail, PostAdd, PostEdit and delete_post


class CategoryList(generic.ListView):
    """View to render the category list"""
    model = Category
    template_name = 'index.html'
    paginate_by = 6

    def get_context_data(self, **kwargs):
        context = super(CategoryList, self).get_context_data(**kwargs)
        context['posts'] = Post.objects.order_by('-created')
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
    """ View to render detail for a chosen post """
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
                                 'Comment successfully added!')

        else:
            comment_form = CommentForm()
            messages.add_message(request, messages.SUCCESS,
                                 'Comment not added, too many characters!')

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


@method_decorator(login_required, name='post')
class PostAdd(View):
    """ View to allow adding of new posts """
    def get(self, request, *args, **kwargs):
        model = Post
        template_name = 'add_post.html'

        return render(
            request,
            'add_post.html',
            {
                'post_add_form': PostAddForm()
            }
        )

    def post(self, request, *args, **kwargs):
        letterstr = string.ascii_lowercase
        slugval = ''.join(random.choice(letterstr) for i in range(6))

        post_add_form = PostAddForm(data=request.POST)

        if post_add_form.is_valid():
            post = post_add_form.save(commit=False)
            post.author = request.user
            post.slug = slugval
            if len(request.FILES) != 0:
                post.image = request.FILES['image']

            post.save()
            messages.add_message(request, messages.SUCCESS,
                                 'Post successfully added!')

            return redirect(reverse('post_detail', args=[post.id]))

        else:
            messages.add_message(request, messages.WARNING,
                                 'Post not added. Please see ' +
                                 '"Guidance on creating posts."')

            return redirect(reverse('add_post'))


@method_decorator(login_required, name='post')
class PostEdit(View):
    """ View to allow editing of existing posts """
    def get(self, request, id, *args, **kwargs):
        queryset = Post.objects
        post = get_object_or_404(queryset, id=id)
        comments = post.post_comments.order_by('created')
        liked = False

        if post.likes.filter(id=self.request.user.id).exists():
            liked = True

        return render(
            request,
            'edit_post.html',
            {
                'liked': liked,
                'post_edit_form': PostEditForm(instance=post)
            }
        )

    def post(self, request, id, *args, **kwargs):
        queryset = Post.objects
        post = get_object_or_404(queryset, id=id)
        comments = post.post_comments.order_by('created')
        liked = False

        post_edit_form = PostEditForm(request.POST, instance=post)

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
                                     'Post not amended. Please see ' +
                                     '"Guidance on editing posts."')

            return redirect(reverse('post_detail', args=[post.id]))


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

    def post(self, request, *args, **kwargs):

        contact_us_form = ContactForm(data=request.POST)

        if contact_us_form.is_valid():
            contact_us_form.save()
            messages.add_message(request, messages.SUCCESS,
                                 'Thanks for your message!')

        else:
            contact_us_form = ContactForm()
            messages.add_message(request, messages.WARNING,
                                 'Message not sent. Please see ' +
                                 '"Guidance on submitting messages."')

        return render(
            request,
            'contact_us.html',
            {
                'contact_us_form': ContactForm()
            }
        )
