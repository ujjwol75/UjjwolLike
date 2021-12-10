from django.http.response import HttpResponse
from django.shortcuts import render
from .models import Post, Like
# Create your views here.



def index(request):
    post = Post.objects.all()
    return render(request, 'app/like.html', {'post':post})

def Like_Page(request):
    if request.method == 'GET':
        post_id = request.GET['post_id']
        print(post_id)
        likedpost = Post.objects.get(id=post_id)
        print(likedpost)
        m = Like(post=likedpost)
        m.save()
        return HttpResponse('success')
    else:
        return HttpResponse('unsuccessful')

