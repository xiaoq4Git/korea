from django.shortcuts import render,render_to_response
from django.template import Context, loader
from django.http import HttpResponse

# Create your views here.

'''
def index(request):
    template = loader.get_template('bbs/index.html')
    c = Context({})
    return HttpResponse(template.render(c))
'''
def index(request):
    return render_to_response('bbs/index.html')
