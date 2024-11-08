from django.shortcuts import render
from FilterApp.models import FilterModel 
# Create your views here.

def upper_view(request):
    data_list=FilterModel.objects.all()
    return render(request,'FilterApp/upper.html',{'data_list': data_list})

def lower_view(request):
    data_list=FilterModel.objects.all()
    return render(request,'FilterApp/lower.html',{'data_list':data_list})

def title_view(request):
    data_list=FilterModel.objects.all()
    return render(request,'FilterApp/title.html',{'data_list':data_list})