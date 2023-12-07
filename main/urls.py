from django.urls import path
from .views import index, category_view, detail_view, search_view, authors, author_posts, home, about


urlpatterns = [
    path('', home, name='index'),
    path('post/<int:post_id>', detail_view, name='post_detail'),
    path('category/<int:category_id>', category_view, name='category_view'),
    path('search/', search_view, name='search'),
    path('authors/', authors, name='authors'),
    path('author/<int:pk>/posts', author_posts, name='author_posts'),
    path('blog/', index, name='blog' ),
    path('about/', about, name='about'),
]

handler404 = 'main.views.page_not_found'