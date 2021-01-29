from django.shortcuts import get_object_or_404
from django.template import loader
from django.http import HttpResponse
from .models import Post

def index(request):
    context = {}
    context['page'] = 'index'

    html_template = loader.get_template('front-end/index.html')
    return HttpResponse(html_template.render(context, request))

def insight(request):
    context = {}
    posts = Post.objects.all()
    latest = posts.order_by('-id')[:4]
    latest_first = latest[0:2]
    latest_second = latest[2:4]
    popular = posts.filter(tags__name__in=["popular"])[:6]
    hot = posts.filter(tags__name__in=["hot"])[:6]
    recommended = posts.filter(tags__name__in=["recommended"])[:6]
    another = posts.filter(tags__name__in=["another"])[:4]
    context['latest_first'] = latest_first
    context['latest_second'] = latest_second
    context['popular'] = popular
    context['hot'] = hot
    context['recommended'] = recommended
    context['another'] = another

    html_template = loader.get_template('front-end/insights/index.html')
    return HttpResponse(html_template.render(context, request))

def insight_post(request,id):

    context = {}
    post = get_object_or_404(Post, pk=id)

    posts = Post.objects.all()
    latest = posts.order_by('-id')[:4]
    popular = posts.filter(tags__name__in=["popular"])[:2]
    context['latest'] = latest
    context['popular'] = popular

    if post:
        context['post'] = post
        context['latest'] = latest
        context['popular'] = popular
    html_template = loader.get_template('front-end/insights/post-page.html')
    return HttpResponse(html_template.render(context, request))
