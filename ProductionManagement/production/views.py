from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Production

# Create your views here.
def production_list(request):
    posts = Production.objects.filter(created_at__lte=timezone.now()).order_by('created_at')

    return render(request, 'production/production_list.html', {'posts': posts}) 

def post_detail(request, pk):
	post = get_object_or_404(Post, pk=pk)
	return render(request, 'blog/post_detail.html', {'post': post})