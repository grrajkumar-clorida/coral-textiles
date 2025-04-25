from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Production
from .forms import DailyProductionReportForm
from django.utils import timezone
from django.contrib import messages

# Create your views here.
def production_list(request):
    posts = Production.objects.filter(created_at__lte=timezone.now()).order_by('created_at')

    return render(request, 'production/production_list.html', {'posts': posts}) 

def post_detail(request, pk):
	post = get_object_or_404(Post, pk=pk)
	return render(request, 'blog/post_detail.html', {'post': post})

# Daily Production Status Report
def dpsr_log(request):    
    if request.method == 'POST':
        form = DailyProductionReportForm(request.POST, request.FILES)
        if form.is_valid():
            dpsrdata = form.save(commit=False)
            dpsrdata.save()
            messages.success(request, 'Daily Production Report Saved!')
            return redirect('dpsr_log')
        else:
        	messages.error(request, 'Please correct the errors below.')
        	print(list(request.POST.items()))
            
    else:
        form = DailyProductionReportForm()
    return render(request, 'production/dpsr.html', {'form': form})

