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
            received_date = form.save(commit=False)

            received_date.user = request.User
            received_date.save()
            messages.success(request,'data is added')

