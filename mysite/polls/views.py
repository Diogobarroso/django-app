from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import redirect
from django.template import loader
from .forms import PostForm
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
from django.forms.utils import ErrorList

from .models import User



def list(request):
    user_list = User.objects.all()
    template = loader.get_template('polls/list.html')
    context = {'user_list': user_list}
    return HttpResponse(template.render(context, request))

def index(request):
    user_list = User.objects.all()
    template = loader.get_template('polls/index.html')
    context = {}
    return HttpResponse(template.render(context, request))

def nameExists(name):
    for u in User.objects.all():
        if name == u.name:
            return True 

    return False

def emailExists(email):
    for u in User.objects.all():
        if email == u.email:
            return True 

    return False

def add(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            if(not nameExists(user.name)):
                if(not emailExists(user.email)):
                    try:
                        validate_email(user.email)
                    except  ValidationError:
                        form._errors["email"] = ErrorList([u"Insert a valid email"])
                        return render(request, 'polls/add.html', {'form': form}) #return the form with an error
                    else:
                        user.save()
                else:
                    form._errors["email"] = ErrorList([u"That email is already registered!"])
                    return render(request, 'polls/add.html', {'form': form}) #return the form with an error
            else:
                form._errors["name"] = ErrorList([u"That name is already registered!"])
                return render(request, 'polls/add.html', {'form': form}) #return the form with an error
            return redirect('list')
    else:
        form = PostForm()
    return render(request, 'polls/add.html', {'form': form})