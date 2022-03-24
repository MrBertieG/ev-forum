from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from django.shortcuts import reverse


STATUS = ((0, "Draft"), (1, "Published"))


class Category(models.Model):
    """Schema for the Category model"""
    name = models.CharField(max_length=150, unique=True)
    desc_box = models.TextField()

    def __str__(self):
        return self.name


class Post(models.Model):
    """Schema for Post model"""
    title = models.CharField(max_length=150, unique=True)
    slug = models.SlugField(max_length=150, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE,
                               related_name="user_posts")

    updated = models.DateTimeField(auto_now=True)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    image = CloudinaryField("image", default='placeholder')
    excerpt = models.TextField(blank=True)
    status = models.IntegerField(choices=STATUS, default=0)
    likes = models.ManyToManyField(
        User, related_name='blogpost_like', blank=True)

    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, related_name="category_posts")

    def __str__(self):
        return self.title

    class Meta:
        """Sorts the posts in descending order"""
        ordering = ["-created"]

    def number_of_likes(self):
        return self.likes.count()


class Comment(models.Model):
    """Schema for the Comment model"""
    body = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE,
                               related_name="user_comments")
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    image = CloudinaryField("image", blank=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE,
                             related_name="post_comments")

    def __str__(self):
        return f"Comment {self.body} by {self.author}"

    class Meta:
        """Comments in descending order"""
        ordering = ["-created"]


class Contact(models.Model):
    """Schema for the Contact page model, to be used in the contact form"""
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.EmailField()
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Message {self.body} from {self.first_name} {self.last_name}"
