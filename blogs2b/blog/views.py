from django.shortcuts import render
from django.http import HttpResponse
from django.utils import timezone
from .models import Post

# Create your views here.

def index(request):
    posts = Post.objects.filter(published_date__lte=timezone.now())
    return render(request, 'index.html', {'posts': posts})
