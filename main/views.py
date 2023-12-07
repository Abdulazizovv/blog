from django.shortcuts import render
from .models import Event, Category, Post, Author
from django.db.models import Q


def home(request):
    return render(request, 'home.html')


def about(request):
    return render(request, 'about.html')


def index(request):
    events = Event.objects.all()
    categories = Category.objects.all()
    posts = Post.objects.all().order_by('-reg_date')[:10]
    return render(request, 'index.html', {'events': events, 'categories': categories, 'posts': posts})


def category_view(request, category_id):
    if category_id == 0:
        categories = Category.objects.all()
        category = ''
        posts = Post.objects.all()
        return render(request, 'index.html', {'posts': posts , 'category': category, 'categories': categories})
    try:
        categories = Category.objects.all()
        category = Category.objects.get(id=category_id)
        posts = Post.objects.filter(category=category_id)
        return render(request, 'index.html', {'posts': posts , 'category': category, 'categories': categories})
    except Category.DoesNotExist:
        print('error: Category not found')
        return render(request, '404.html')


def detail_view(request, post_id):
    try:
        post = Post.objects.get(id=post_id)
        return render(request, 'detail.html', {'post': post})
    except Post.DoesNotExist:
        return render(request, '404.html')


def search_view(request):

    query = request.GET.get('query')
    posts = Post.objects.filter(
            Q(title__icontains=query) |  
            Q(text__icontains=query)
        ).distinct() 

    return render(request, 'search.html', {'posts': posts})


def authors(request):
    authors = Author.objects.all()
    return render(request, 'authors.html', {'authors': authors})


def author_posts(request, pk):
    try:
        author = Author.objects.get(pk=pk)
        posts = Post.objects.filter(author=author)
        return render(request, 'author_posts.html', {'posts': posts})
    except author.DoesNotExist:
        print("Post author not found")


def page_not_found(request, exception):
    return render(request, '404.html', status=404)