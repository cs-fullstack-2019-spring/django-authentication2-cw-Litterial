from django.shortcuts import render, HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Blog


# Create your views here.
@login_required  #requires user to login
def index(request):
    userBlog = Blog.objects.filter(username=request.user)  #filters username request
    context = {'myBlog': userBlog}
    return render (request,'cwApp/index.html',context)  #goes to index in templates