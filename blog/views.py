from django.shortcuts import render, get_object_or_404
from .models import Post
from django.utils import timezone

# View for listing all posts
def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)  # this raises 404 if not found
    return render(request, 'blog/post_detail.html', {'post': post})