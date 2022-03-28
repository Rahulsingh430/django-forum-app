from urllib import request
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Post
from .forms import PostForm
# Create your views here.


def index(request):
    # IF THE METHOD IS POPST
    if request.method == 'POST':
        form = PostForm(request)
    # IF THE FORM IS VALID
        if form.is_valid():
         # YES, SAVE
            form.save()
         # REDIRECT TO HOME
            return HttpResponseRedirect('/')

        else:
            # NO, SHOW ERROR
            return HttpResponseRedirect(form.error.as_json())

    # GET ALL POST LIMIT=20
    posts = Post.objects.all()[:20]
 # Show
    return render(request, 'posts.html', {'posts': posts})
