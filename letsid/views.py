import datetime
from django.utils.timezone import utc
from django.http import StreamingHttpResponse
from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import logout, authenticate, login
from .forms import UserCreationForm
from sosmed.models import sosmed
from sosmed_comment.models import sosmedComment
from sosmed_comment.forms import ssmdcmntForm
from berita.models import postBerita
from berita_comment.models import beritaComment
from berita_comment.forms import brtcmntForm
from kultur.models import kulturPost
from kultur_comment.models import kulturComment
from kultur_comment.forms import kltrcmntForm

def index(request):
    posts = sosmed.objects.filter().order_by('-id')

    context ={
      'judul':'LetsId',
      'content':'Wellcome to my web.',
      'webname': 'letsId',
      'post': posts,
    }

    return render(request, 'index.html', context)

def singlePost(request, slugInput):
    posts = sosmed.objects.get(slug=slugInput)
    comments = sosmedComment.objects.all()
    form = ssmdcmntForm()

    context ={
      'judul':'LetsId',
      'content':'Wellcome to my web.',
      'webname': 'LetsId',
      'p_judul' : posts.judul,
      'p_img' : posts.media,
      'p_body' : posts.body,
      'p_kategori': posts.category,
      'p_slug': posts.slug,
      'p_lokasi': posts.lokasi,
      'comments': comments,
      'form': form
    }

    if request.method == "POST":
        Ucomment = request.POST['comment']
        username = request.user.username
        forSosmed = posts.slug

        sosmedComment.objects.create(
            forSosmed = forSosmed,
            user = username,
            comment = Ucomment
        )

    return render(request, 'sosmed.html', context)

def berita(request):
    posts = postBerita.objects.filter().order_by('-id')

    context ={
      'judul':'LetsId',
      'content':'Wellcome to my web.',
      'webname': 'letsId',
      'post': posts,
    }

    return render(request, 'berita.html', context)

def brtsinglePost(request, slugInput):
    posts = postBerita.objects.get(slug=slugInput)
    comments = beritaComment.objects.all()
    form = brtcmntForm()

    context ={
      'judul':'LetsId',
      'content':'Wellcome to my web.',
      'webname': 'LetsId',
      'p_judul' : posts.judul,
      'p_img' : posts.media,
      'p_body' : posts.body,
      'p_kategori': posts.category,
      'p_slug': posts.slug,
      'p_lokasi': posts.lokasi,
      'comments': comments,
      'form': form
    }

    if request.method == "POST":
        Ucomment = request.POST['comment']
        username = request.user.username
        forBerita = posts.slug

        beritaComment.objects.create(
            forBerita = forBerita,
            user = username,
            comment = Ucomment
        )

    return render(request, 'brtsp.html', context)

def kultur(request):
    posts = kulturPost.objects.filter().order_by('-id')

    context ={
      'judul':'LetsId',
      'content':'Wellcome to my web.',
      'webname': 'letsId',
      'post': posts,
    }

    return render(request, 'kultur.html', context)

def kltrsinglePost(request, slugInput):
    posts = kulturPost.objects.get(slug=slugInput)
    comments = kulturComment.objects.all()
    form = kltrcmntForm()

    context ={
      'judul':'LetsId',
      'content':'Wellcome to my web.',
      'webname': 'LetsId',
      'p_judul' : posts.judul,
      'p_img' : posts.media,
      'p_body' : posts.body,
      'p_kategori': posts.category,
      'p_slug': posts.slug,
      'p_lokasi': posts.lokasi,
      'comments': comments,
      'form': form
    }

    if request.method == "POST":
        Ucomment = request.POST['comment']
        username = request.user.username
        forKultur = posts.slug

        kulturComment.objects.create(
            forKultur = forKultur,
            user = username,
            comment = Ucomment
        )

    return render(request, 'kltrsp.html', context)

def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            login(request, user)
            return redirect("userdata")

        else:
            for msg in form.error_messages:
                print(form.error_messages[msg])

            return render(request = request,
                          template_name = "main/register.html",
                          context={"form":form})

    form = UserCreationForm

    context={
        'form': form,
    }
    return render(request, "main/register.html", context)