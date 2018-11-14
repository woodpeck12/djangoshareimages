from django.shortcuts import render,redirect

# Create your views here.
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import ShareImageCreateForm


@login_required
def shareimage_create(request):
    if request.method == 'POST':
        form = ShareImageCreateForm(request.POST)
        if form.is_valid():
            cleaned_data = form.cleaned_data
            received_data = form.save(commit=False)

            received_data.user = request.user
            received_data.save()
            messages.success(request,'data is added')

            return redirect(received_data.get_absolute_url())
    else:
         form = ShareImageCreateForm(data=request.GET)

    return render(request,"shareimage/image/create.html",{'section':'images','form':form})

