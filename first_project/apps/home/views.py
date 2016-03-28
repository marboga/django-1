from django.shortcuts import render, HttpResponse

def index(request):
    context = {
        'data': [
            {'id': 'name', 'content': 'Michael Arbogast'},
            {'id': 'favorite game', 'content': 'Ultimate Frisbee'},
            {'id': 'favorite language', 'content': 'Python with Django'},
        ]
    }
    return render(request, 'home/index.html', context)

# Create your views here.
