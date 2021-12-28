from django.shortcuts import redirect, render
from blog.forms import PostForm
from blog.models import Post

# Create your views here.
def post_list(request):
    qs = Post.objects.all()
    context = {
        "object_list":qs,
    }
    return render(request,"blog/post_list.html",context)

def post_create(request):
    form = PostForm()
    if request.method == "POST":
        form= PostForm(request.POST,request.FILES)
    # form = PostForm(request.POST or None,request.FILES or None)
        if form.is_valid():
            post=form.save(commit=False)
            post.author=request.user
            post.save()
            return redirect('blog:list')
            
    context = {
        "form":form,
    }
    return render(request,"blog/post_create.html",context)