from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Post, MovieDetails, MovieDirector
from django.db.models import Q


# Create your views here.

def post_list(request):
    cat = request.GET.get('cat', '')
    txt = request.GET.get('txt', '')
    try:
        cat = int(cat)
    except:
        cat = False

    if not cat:  # cat == False
        if txt == '':
            post = Post.objects.filter(published_date__lte=timezone.now()). \
                order_by('published_date')
        else:
            post = Post.objects.filter((Q(movie_details__title__contains=txt)) &
                                       Q(published_date__lte=timezone.now())).order_by(
                                        'published_date')
    else:
        post = Post.objects.filter(published_date__lte=timezone.now()).filter(movie_details=cat)\
            .order_by(
            'published_date')
    return render(request, 'blog/post_list.html', {'post': post})


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})


def movie_director(request, pk):
    post = get_object_or_404(MovieDirector, pk=pk)
    # post = MovieDirector.surname
    return render(request, 'blog/movie_director.html', {'post': post})
