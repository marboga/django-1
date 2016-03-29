from django.http import  Http404, HttpResponseNotFound, HttpResponse
from django.shortcuts import render

def index(request, ninja_color):
    context = {
        # "color": '<img src="/static/ninja/michelangelo.jpg"  alt="michelangelo" /><img src="/static/ninja/donatello.jpg" alt="donatello" /><img src="/static/ninja/leonardo.jpg" alt="leonardo" /><img src= "/static/ninja/raphael.jpg" alt="raphael" />'
    }
    print ninja_color, "ninja color"
    if ninja_color == 'orange':
        context = {
        "color": '<img src="/static/ninja/michelangelo.jpg"  alt="michelangelo" />'
        }
    elif ninja_color == 'purple':
        context = {
        "color": '<img src="/static/ninja/donatello.jpg" alt="donatello" />'
        }
    elif ninja_color == 'blue':
        context = {
        "color": '<img src="/static/ninja/leonardo.jpg" alt="leonardo" />'
        }
    elif ninja_color == 'red':
        context = {
        "color": '<img src= "/static/ninja/raphael.jpg" alt="raphael" />'
        }
    else:
        context = {
        "color": '<img src="/static/ninja/notapril.jpg" alt="april o\' neal">'
        }
    return render(request, 'ninja/index.html', context)

def show(request):
    context = {
    "color": '<img src="/static/ninja/michelangelo.jpg"  alt="michelangelo" /> <img src="/static/ninja/donatello.jpg" alt="donatello" /> <img src="/static/ninja/leonardo.jpg" alt="leonardo" /> <img src= "/static/ninja/raphael.jpg" alt="raphael" />'
    }
    return render(request, 'ninja/index.html', context)

# def show(request):
#     context = {
#     "april": 'img src="/static/ninja/april.jpg" alt="april o\' neal"'
#     }
