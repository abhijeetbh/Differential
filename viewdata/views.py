from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# Create your views here.
def sample(request):
    template=loader.get_template('viewdata/index.html')
    context={'key':'value'}
    return HttpResponse(template.render(context, request))