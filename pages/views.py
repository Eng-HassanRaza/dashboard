from django.shortcuts import render
from .models import Pricing_Page,Impacx_Page,Digitialization_Page
from main.models import Pricing,Post,Pricing_Features_Value,Pricing_Packages
from django.template import loader
from django.http import HttpResponse,JsonResponse
# Create your views here.
def web_hosting(request):
    context = {}
    pricing = Pricing.objects.filter(pricing_page__page_path='web_hosting')
    pricing_page = Pricing_Page.objects.filter(page_path="web_hosting").first()
    context['pricing'] = pricing
    context['pricing_page'] = pricing_page
    html_template = loader.get_template('front-end/insights/pricing.html')
    return HttpResponse(html_template.render(context, request))

def reseller_hosting(request):
    context = {}
    pricing = Pricing.objects.filter(pricing_page__page_path='reseller_hosting')
    pricing_page = Pricing_Page.objects.filter(page_path="reseller_hosting").first()
    context['pricing'] = pricing
    context['pricing_page'] = pricing_page
    html_template = loader.get_template('front-end/insights/pricing.html')
    return HttpResponse(html_template.render(context, request))

def impacx_page(request):
    context = {}
    impacx_obj = Impacx_Page.objects.first()
    latest_posts = Post.objects.all().order_by('-id')[:4]
    context['impacx_data'] = impacx_obj
    context['latest_posts'] = latest_posts
    html_template = loader.get_template('front-end/insights/impax-page.html')
    return HttpResponse(html_template.render(context, request))

def pricing_page_reseller(request):
    context = {}
    pricing_features_values_obj = Pricing_Features_Value.objects.filter(
        pricing_features__pricing_page__page_path="reseller_hosting")
    pricing_packages = Pricing_Packages.objects.filter(pricing_page__page_path="reseller_hosting")
    features = pricing_features_values_obj.all().values_list('pricing_features__feature_name', flat=True).distinct()
    reseller_hosting_objs = pricing_features_values_obj.filter(pricing_features__pricing_page__page_path="reseller_hosting")
    context['pricing_packages'] = pricing_packages
    context['features_values'] = reseller_hosting_objs
    context['features'] = features

    html_template = loader.get_template('front-end/pricing/index.html')
    return HttpResponse(html_template.render(context, request))

def pricing_page_webhosting(request):
    context = {}
    pricing_features_values_obj = Pricing_Features_Value.objects.filter(pricing_features__pricing_page__page_path="web_hosting")
    pricing_packages = Pricing_Packages.objects.filter(pricing_page__page_path="web_hosting")
    features = pricing_features_values_obj.all().values_list('pricing_features__feature_name', flat=True).distinct()
    reseller_hosting_objs = pricing_features_values_obj.filter(pricing_features__pricing_page__page_path="web_hosting")
    context['pricing_packages'] = pricing_packages
    context['features_values'] = reseller_hosting_objs
    context['features'] = features

    html_template = loader.get_template('front-end/pricing/index.html')
    return HttpResponse(html_template.render(context, request))

def Digitialization_page(request):
    context = {}
    impacx_obj = Digitialization_Page.objects.first()
    latest_posts = Post.objects.all().order_by('-id')[:4]
    context['impacx_data'] = impacx_obj
    context['latest_posts'] = latest_posts
    html_template = loader.get_template('front-end/insights/impax-page.html')
    return HttpResponse(html_template.render(context, request))