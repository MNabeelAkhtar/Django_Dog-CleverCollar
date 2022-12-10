from django.shortcuts import render, redirect
from datetime import date
from .models import Post, User
from django.contrib import messages
from .forms import SignUpForm

# Create your views here.


def home(request):
    if request.method == 'GET':
        SignUp = SignUpForm()
    else:
        SignUp = SignUpForm(request.POST)
        if SignUp.is_valid():
            user_email = SignUp.cleaned_data['email']
            user, was_created = User.objects.get_or_create(email=user_email)
            return redirect('confirm_signup')

    return render(request, "home/home.html",{
        'form': SignUp
    })


def post(request):
    allPosts = Post.objects.all()
    return render(request, "home/all-post.html", {"posts": allPosts})

def create_post(request):
    if request.method == "POST":
        name = request.POST['dog_name']
        age = request.POST['dog_age']
        breed = request.POST['dog_breed']
        owner_name = request.POST['owner_name']
        title = request.POST['title']
        author = request.POST['author']
        excerpt = request.POST['excerpt']
        content = request.POST['content']
        date = request.POST['date']
        image = request.POST['image']
        sec_image = request.POST['sec_image']
        mor_image = request.POST['mor_image']
        slug = title.lower().replace(" ", "-")
        print(slug, title, name)
        Post.objects.create(name=name, age=age, breed=breed, owner_name=owner_name, title=title,
                            author=author, excerpt=excerpt, content=content, date=date, slug=slug,
                            image=image, sec_image=sec_image, mor_image=mor_image)
        return render(request, "home/create_post.html")
    else:
        return render(request, "home/create_post.html")

def add_post(request):
    Post.objects.create()
    # messages.success(request, 'Post Added Successfully')
    return redirect("home/create_post.html")


def post_detail(request, post_slug):
    clicked_post = Post.objects.get(slug=post_slug)
    return render(request, "home/post-detail.html", {"post": clicked_post})


def delete_post(request, post_slug):
    clicked_post = Post.objects.get(slug=post_slug)
    clicked_post.delete()
    # messages.success(request, 'Post Delete Successfully')
    return redirect("/posts")


def confirm_signup(request):
    return render(request, 'home/SignUp_Confirmation.html')



