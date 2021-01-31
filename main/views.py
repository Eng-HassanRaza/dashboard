from django.shortcuts import get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from django.template import loader
from django.http import HttpResponse,JsonResponse
from .models import Post,Slider,Catagory

def index(request):
    context = {}
    sliders = Slider.objects.all()
    catagories = Catagory.objects.all()
    posts = Post.objects.all().order_by('-id')
    latest = posts[:3]
    context['page'] = 'index'
    data = {'latest': latest, 'slider_data': sliders,'questions':catagories}
    context['data'] = data

    html_template = loader.get_template('front-end/index.html')
    return HttpResponse(html_template.render(context, request))
def slider(request):
    context={}
    html_template = loader.get_template('front-end/insights/slider.html')
    return HttpResponse(html_template.render(context, request))
def insight(request):
    context = {}
    posts = Post.objects.all().order_by('-id')
    latest = posts[:4]
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

    posts = Post.objects.all().order_by('-id')
    latest = posts[:4]
    popular = posts.filter(tags__name__in=["popular"])[:2]
    context['latest'] = latest
    context['popular'] = popular

    if post:
        context['post'] = post
        context['latest'] = latest
        context['popular'] = popular
    html_template = loader.get_template('front-end/insights/post-page.html')
    return HttpResponse(html_template.render(context, request))


def insight_catagory(request,catagory):

    context = {}
    id=1
    posts = Post.objects.all().order_by('-id')
    catagory_posts = posts.filter(catagory__name=catagory)
    latest = posts[:4]
    popular = posts.filter(tags__name__in=["popular"])[:2]
    context['latest'] = latest
    context['catagory_name'] = catagory
    context['popular'] = popular

    if posts:
        context['latest'] = latest
        context['catagory_posts'] = catagory_posts
    html_template = loader.get_template('front-end/insights/category.html')
    return HttpResponse(html_template.render(context, request))
@csrf_exempt
def insight_question_answer(request):
    context = {}
    data = dict()
    ansone = request.POST['answerone']
    anstwo = request.POST['answertwo']
    posts = Post.objects.all().order_by('-id')
    catagory_posts = posts.filter(catagory__name=ansone)[:3]
    if catagory_posts:
        context['catagory_posts'] = catagory_posts
        html_template = loader.get_template('front-end/parts/question-result.html')
        data['html_table'] = html_template.render(
            context,
            request=request
        )
    else:
        data['html_table'] = '<h2 style="text-align:center;top:20%">No Data Found For Selected Catagory</h2>'


    return JsonResponse(data)

def success_stories(request):
    context = {}
    html_template = loader.get_template('front-end/insights/success_stories.html')
    return HttpResponse(html_template.render(context, request))