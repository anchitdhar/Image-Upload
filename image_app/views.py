from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import *

# Create your views here.

def hotel_image_views(request):
    if request.method == 'POST':
        form = HotelForm(request.POST, request.FILES)

            if form.is_valid():
                form.save()
                return redirect('Success')
            else:
                form = HotelForm()
            return render(request,'hotel_image_form.html',{'form':form})

def Success(request):
    return HttpResponse('successfully uploaded')