from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Post, Category
from django.http import Http404


def index(request):
    posts = Post.objects.filter(
        is_published=True,
        pub_date__lte=timezone.now(),
        category__is_published=True
    ).order_by('pub_date')[:5]
    template = 'blog/index.html'
    context = {'post_list': posts}
    return render(request, template, context)


def post_detail(request, id):
    # Получаем публикацию по первичному ключу
    post = get_object_or_404(Post, id=id, is_published=True,
                             pub_date__lte=timezone.now())
    
    if post.category and not post.category.is_published:
        # Если категория не опубликована, возвращаем 404
        raise Http404("Категория этого поста снята с публикации.")

    template = 'blog/detail.html'
    context = {'post': post}
    return render(request, template, context)


def category_posts(request, category_slug):
    category = get_object_or_404(Category, slug=category_slug,
                                 is_published=True)

    posts = Post.objects.filter(
        category=category,
        pub_date__lte=timezone.now(),
        is_published=True,
    ).order_by('pub_date')

    template = 'blog/category.html'
    context = {
        'category': category,
        'post_list': posts
    }
    return render(request, template, context)
