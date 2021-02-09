from django.shortcuts import render
from .models import Pricing_Page
from main.models import Pricing
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
    print("success")