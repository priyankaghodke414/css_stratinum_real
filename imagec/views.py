from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from django.shortcuts import render, get_object_or_404
from .forms import PostForm,AlbumForm,EditProfileForm
from .models import Post
from django.shortcuts import redirect
from django.core.urlresolvers import reverse

# Create your views here.
def home(request):
    context = {}
    template = 'home.html'
    return render(request, template, context)

@login_required
def newhome(request):
    user = request.user
    return render(request, 'newhome.html', {'user': user})


def signup1(request):
    context = {}
    template = 'signup1.html'
    return render(request, template, context)


@login_required()
def userProfile(request):
    user = request.user
    context = {'user': user}
    template = 'profile.html'
    return render(request, template, context)


def about(request):
    context = {}
    template = 'about.html'
    return render(request, template, context)


@login_required()
def create_form(request):
        form = AlbumForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            album = form.save(commit=False)
            album.user = request.user
            album.image= request.FILES['image']
            album.save()
            return render(request, 'about.html', {'album': album})
        context = {
            "form": form,
        }
        return render(request, 'create_form.html', context)

def edit_profile(request):
    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance=request.user)

        if form.is_valid():
            form.save()
            return redirect(reverse('about'))
    else:
        form = EditProfileForm(instance=request.user)
        args = {'form': form}
        return render(request, 'edit_profile.html', args)


@login_required
def post_detail(request):
    user = request.user
    return render(request, 'post_detail.html', {'user': user})



@login_required
def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            return redirect('newhome')
    else:
        form = PostForm()
    return render(request, 'post_edit.html', {'form': form})



@login_required
def post_edit(request):
    post = get_object_or_404(Post)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            user = request.user
            return render(request, 'newhome.html', {'user': user})
    else:
        form = PostForm(instance=post)
    return render(request, 'newhome.html', {'form': form})
