from django.shortcuts import render
from . import models

def post_view(request):
    if request.method == 'GET':
        post = models.Post.objects.all()
        return render(request, template_name='post.html', context={'post': post})