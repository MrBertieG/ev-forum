from django.shortcuts import render

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

