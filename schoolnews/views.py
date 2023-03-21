from django.shortcuts import render
from django.http import HttpResponse
from schoolnews.models import Page
# Create your views here.

def index(request):

    news_list = Page.objects.all().order_by('-date')

    context_dict = {}
    context_dict['page'] = news_list

    return render(request, 'schoolnews/index.html', context=context_dict)