from django.shortcuts import render, redirect, get_object_or_404
from .forms import PostForm, CommentForm
from .models import Post, Comment

def post_list(request):
    post_list = Post.objects.all()
    return render(request, 'myapp/post_list.html', {
        'post_list': post_list
    })

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'myapp/post_detail.html', {
        'post': post
    })

def post_new(request):
    form_cls = PostForm
    template_name = 'myapp/post_form.html'
    success_url = '/'

    if request.method == 'POST':
        form = form_cls(request.POST, request.FILES)
        if form.is_valid():
            post = form.save()
            return redirect(post)
    else:
        form = form_cls()

    return render(request, template_name, {
        'form': form,
    })


def post_edit(request, pk):
    form_cls = PostForm
    template_name = 'myapp/post_form.html'
    success_url = '/'

    post = get_object_or_404(Post, pk=pk)

    if request.method == 'POST':
        form = form_cls(request.POST, request.FILES, instance=post)
        if form.is_valid():
            post = form.save()
            return redirect(success_url)
    else:
        form = form_cls(instance=post)

    return render(request, template_name, {
        'form': form,
    })


def comment_new(request, post_pk):
    form_cls = CommentForm
    template_name = 'myapp/comment_form.html'
    success_url = '/'

    post = get_object_or_404(Post, pk=post_pk)

    if request.method == 'POST':
        form = form_cls(request.POST, request.FILES)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.ip = request.META['REMOTE_ADDR']
            comment.save()
            return redirect(success_url)
    else:
        form = form_cls()

    return render(request, template_name, {
        'form': form,
    })


def comment_edit(request, post_pk, pk):
    form_cls = CommentForm
    template_name = 'myapp/comment_form.html'
    success_url = '/'

    comment = get_object_or_404(Comment, pk=pk)

    if request.method == 'POST':
        form = form_cls(request.POST, request.FILES, instance=comment)
        if form.is_valid():
            comment = form.save()
            return redirect('/')
    else:
        form = form_cls(instance=comment)

    return render(request, template_name, {
        'form': form,
    })
