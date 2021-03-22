from django.shortcuts import render, get_object_or_404, redirect
from .models import *
from .forms import UserRegister, UserLogin, AddImage
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.core.paginator import Paginator
from django.forms import formset_factory, inlineformset_factory


def home(request):
    images = Image.objects.all().order_by('-id')
    tags = Tags.objects.all()


    paginator = Paginator(images, 6)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    if request.method == 'POST':
        tag = request.POST['filter']
        tags = Tags.objects.all()
        result = Image.objects.filter(tags=tag)
        context = {
            'result': result,
            'tags': tags,


        }
        return render(request, 'mygallery/home.html', context)

    context = {
        'images': page_obj,
        'tags': tags,
        'page_obj': page_obj,

    }
    return render(request, 'mygallery/home.html', context)


def register(request):
    form = UserRegister

    if request.method == 'POST':
        form = UserRegister(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, 'Account successfully created for' + username)
            return redirect('my_gallery:login')

    context = {'form': form}
    return render(request, 'mygallery/register.html', context)


def user_login(request):
    form = UserLogin
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('my_gallery:home')
        else:
            messages.info(request, 'Username or Password Incorrect')

    context = {'form': form}
    return render(request, 'mygallery/login.html', context)


def user_logout(request):
    logout(request)
    return redirect('my_gallery:home')


def add_image(request):
    #AddImageFormSet = formset_factory(AddImage, extra=3, max_num=3)
    #formset = AddImageFormSet()
    form = AddImage
    if request.method == 'POST':
        form = AddImage(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Image Successfully Add')
            return redirect('my_gallery:home')
    context = {
        'form': form
    }
    return render(request, 'mygallery/add_image.html', context)
