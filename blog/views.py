from django.shortcuts import render
from django.utils import timezone
from .models import Post


def post_list(request):
    posts = Post.objects.filter(pdate = timezone.now()).order_by('pdate')
    return render(request , 'blog/post_list.html', {'posts': posts})
# Create your views here.
