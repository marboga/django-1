from django.shortcuts import render
from django.http import HttpResponse

def noninja(request):
    return HttpResponse("No Ninjas Here. Try looking at /ninja")
