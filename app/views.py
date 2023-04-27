from django.shortcuts import render
import datetime
# Create your views here.
def built_in_filters(request):
    dt=datetime.datetime.now()
    d={'data':'HAi hOw Are YoU','dt':dt,'c':10}
    return render(request,'built_in_filters.html',d)