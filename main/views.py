from django.shortcuts import get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from django.template import loader
from django.http import HttpResponse,JsonResponse
from .models import Post,Slider,Catagory,Success_Stories,Pricing,Team
from django.shortcuts import render

def index(request):
    context = {}
    sliders = Slider.objects.all()
    catagories = Catagory.objects.all()
    posts = Post.objects.all().order_by('-id')
    latest = posts[:3]
    success_stories = Success_Stories.objects.all()
    success_stories = success_stories[:3]
    context['page'] = 'index'
    data = {'latest': latest, 'slider_data': sliders,'questions':catagories,'success_stories':success_stories}
    context['data'] = data
    html_template = loader.get_template('front-end/index.html')
    return HttpResponse(html_template.render(context, request))
def contact_us(request):
    context={}
    html_template = loader.get_template('front-end/insights/contact-us.html')
    return HttpResponse(html_template.render(context, request))
def pricing(request):
    context={}
    pricing =Pricing.objects.all()
    context['pricing']=pricing
    html_template = loader.get_template('front-end/insights/pricing.html')
    return HttpResponse(html_template.render(context, request))

def portfolio(request):
    context={}
    html_template = loader.get_template('front-end/insights/portfolio.html')
    return HttpResponse(html_template.render(context, request))

def team(request):
    context={}
    team=Team.objects.all()
    context['team']=team
    html_template = loader.get_template('front-end/insights/team.html')
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

@csrf_exempt
def success_stories(request):
    context = {}
    success_stories = Success_Stories.objects.all()
    context['success_stories'] = success_stories
    html_template = loader.get_template('front-end/insights/success_stories.html')
    return HttpResponse(html_template.render(context, request))

def favorite(request):
    context={}
    context = {}
    data = dict()
    bookmark_id = request.POST['bookmark_id']
    post = get_object_or_404(Post, pk=int(bookmark_id))
    post.is_bookmark = True
    post.save()
    red_insight_list = []
    try:
        insight_session_data= request.session['red_insights']
        item_exist = next((item for item in insight_session_data if item["insight_id"] == int(bookmark_id)),False)
        if not item_exist:
            insight_session_data.append({
                "insight_name": post.title,
                "insight_id":post.id
            })
            request.session['red_insights'] = insight_session_data
    except:
        request.session['red_insights'] = [{
            "insight_name": post.title,
            "insight_id":post.id
        }]
    insight_session_data = request.session['red_insights']
    context['insight_data'] = insight_session_data
    html_template = loader.get_template('front-end/parts/red-folder-ajax.html')
    data['html_table'] = html_template.render(
        context,
        request=request
    )
    # del request.session['red_insights']
    return JsonResponse(data)

def bookmark_page(request):
    context = {}
    bookmark_post = []
    latest_post = Post.objects.all().order_by('-id')[:4]
    red_insights_data = request.session['red_insights']
    for ele in red_insights_data:
        post = get_object_or_404(Post, pk=ele['insight_id'])
        bookmark_post.append(post)
    if bookmark_post:
        context['bookmark_posts'] = bookmark_post
    context['latest']=latest_post
    html_template = loader.get_template('front-end/insights/insight-bookmark-page.html')
    return HttpResponse(html_template.render(context, request))

def bookmark_delete_ajax(request):
    context={}
    data = dict()
    bookmark_id = request.POST['bookmark_id']
    d_post = get_object_or_404(Post, pk=bookmark_id)
    d_post.is_bookmark = False
    d_post.save()
    bookmark_data = request.session['red_insights']
    for ele in range(len(request.session['red_insights'])):
        if bookmark_data[ele]['insight_id'] == int(bookmark_id):
            del bookmark_data[ele]
            break
    request.session['red_insights'] = bookmark_data
    request.session.save()
    context['insight_data'] = bookmark_data
    html_template = loader.get_template('front-end/parts/red-folder-ajax.html')
    data['html_table'] = html_template.render(
        context,
        request=request
    )

    bookmark_post = []
    red_insights_data = request.session['red_insights']
    for ele in red_insights_data:
        post = get_object_or_404(Post, pk=ele['insight_id'])
        bookmark_post.append(post)
    if bookmark_post:
        context['bookmark_posts'] = bookmark_post

    html_template2 = loader.get_template('front-end/insights/bookmark-contents.html')
    data['bookmark'] = html_template2.render(
        context,
        request=request
    )
    # del request.session['red_insights']
    return JsonResponse(data)