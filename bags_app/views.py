from django.shortcuts import render
from django.http import HttpResponse
from . import models


def helloView(request):
    return HttpResponse("<h1>Hello Django</h1>")


def postView(request):
    post = models.Post.objects.all()
    html_file = 'post.html'
    context = {
        'post_key': post
    }
    return render(request, html_file, context)
