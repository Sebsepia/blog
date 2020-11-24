from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView
from .models import Post, BlogImage, FreeImage
from django.utils.text import slugify
from datetime import datetime, date

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


class Home(ListView):
    model = Post
    paginate_by = 4
    context_object_name = 'posts'
    template_name = 'home.html'
    ordering = ['-post_date']

class Details(DetailView):
    model = Post
    context_object_name = 'posts'
    template_name = 'details.html'

class Tagged(ListView):
    model = Post
    paginate_by = 4
    context_object_name = 'posts'
    template_name = 'tag.html'
    ordering = ['-id']


#vieille version
def home_view(request):
    posts = range(1, 1000)
    posts = Post.objects.order_by('-id')
    paginator = Paginator(posts, 4)
    freeimgs = FreeImage.objects.all()
    page = request.GET.get('page',1)
    try:
        numbers = paginator.page(page)
    except PageNotAnInteger:
        numbers = paginator.page(1)
    except EmptyPage:
        numbers = paginator.page(paginator.num_pages)
    context = {
    'posts':posts,
    'freeimgs':freeimgs,
    'numbers':numbers,
    }
    return render(request, 'home.html', context)

def detail_view(request, slug):
    post = get_object_or_404(Post, slug=slug)
    freeimgs = FreeImage.objects.all()
    context = {
        'post':post,
        'freeimgs' :freeimgs,
    }
    return render(request, 'details.html', context)

def info_view(request):
    context = {}
    return render(request, 'info.html', context)

def contact_view(request):
    context = {}
    return render(request, 'contact.html', context)

def tagged(request, slug):
    posts = Post.objects.filter(tags__name__in=[slug])
    freeimgs = FreeImage.objects.all()
    context = {
        'posts':posts,
        'freeimgs' :freeimgs,
    }
    return render(request, 'tag.html', context)

def portfolio(request):
    portfolio_catalog = ('test', )
    posts = Post.objects.filter(tags__name__in=portfolio_catalog)
    freeimgs = FreeImage.objects.all()
    context = {
        'posts':posts,
        'freeimgs' :freeimgs,
        'portfolio_catalog': portfolio_catalog,
    }
    return render(request, 'portfolio.html', context)
def nsfw_view(request):

    posts = Post.objects.filter(tags__name__in="nsfw").order_by('-id')
    freeimgs = FreeImage.objects.all()
    context = {
    'posts':posts,
    'freeimgs' :freeimgs,
    }
    return render(request, 'beige.html', context)