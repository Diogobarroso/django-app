from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import redirect
from django.template import loader
from .forms import PostForm

from .models import User



def list(request):
    user_list = User.objects.all()
    template = loader.get_template('polls/list.html')
    context = {'user_list': user_list}
    return HttpResponse(template.render(context, request))

def index(request):
    user_list = User.objects.all()
    template = loader.get_template('polls/index.html')
    context = {'user_list': user_list}
    return HttpResponse(template.render(context, request))

def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.save()
            return redirect('index')
    else:
        form = PostForm()
    return render(request, 'polls/post_new.html', {'form': form})