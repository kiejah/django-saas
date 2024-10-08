from django.http import HttpResponse
from django.shortcuts import render

from visits.models import PageVisit

def home_page_view(request,*args,**kwargs):
    
    qs= PageVisit.objects.all()
    page_qs= PageVisit.objects.filter(path=request.path)
    html_template= "home.html"
    my_title= "My Homepage"
    my_context ={
        "page_title":my_title,
        "page_visit_count":page_qs.count(),
        "total_visit_count":qs.count(),
    }
    
    PageVisit.objects.create(path = request.path)
    return render(request,html_template,my_context)

def about_view(request,*args,**kwargs):
    
    qs= PageVisit.objects.all()
    page_qs= PageVisit.objects.filter(path=request.path)
    html_template= "home.html"
    my_title= "My About Page"
    my_context ={
        "page_title":my_title,
        "page_visit_count":page_qs.count(),
        "total_visit_count":qs.count(),
    }
    
    PageVisit.objects.create(path = request.path)
    return render(request,html_template,my_context)

def old_home_page_view(request,*args,**kwargs):
    return HttpResponse("<h1>Hello JK</h1>")