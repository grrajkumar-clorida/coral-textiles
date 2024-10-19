from django.shortcuts import render, redirect
from .forms import ContactUsForm
from .models import Lead
from django.utils import timezone
from django.contrib import messages

# Create your views here.
def contact_us(request):
    #return render(request, 'home.html')
    if request.method == 'POST':
        form = ContactUsForm(request.POST, request.FILES)
        if form.is_valid():
            contactus = form.save(commit=False)
            contactus.save()
            messages.success(request, 'Your message has been sent successfully. We will reach you soon!')
            return redirect('contact_us')
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = ContactUsForm()
    return render(request, 'vendor/contact_us.html', {'form': form})
