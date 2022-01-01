from django.shortcuts import render, get_object_or_404
from .models import Image
from django.urls import reverse
from django.http import Http404
from django.contrib.auth.models import Permission, User
    

def base_url(request):
    queryset = Image.objects.all().order_by('-id')
    nature = Image.objects.filter(tags='nature').count()
    context = {
        'objectlist' : queryset, 
        "name" : "Home",
        'nat' : nature, 
    }
    return render(request,"home.html", context, x) 

# Create your views here.
def home_view(request):
    queryset = Image.objects.all().order_by('-id')
    listrow1 = Image.objects.filter(row=1)
    listrow2 = Image.objects.filter(row=2)
    listrow3 = Image.objects.filter(row=3)
    listrow4 = Image.objects.filter(row=4)
    nature = Image.objects.filter(tags='nature').count()
    context = {
        "name" : "Home",
        'objectlist' : queryset, 
        'nat' : nature,      
        'row1' : listrow1,
        'row2' : listrow2,
        'row3' : listrow3,
        'row4' : listrow4,
    }
    return render(request, "home.html", context)

def building_view(request):
    queryset = Image.objects.all().order_by('-id')
    listrow1 = Image.objects.filter(row=1)
    listrow2 = Image.objects.filter(row=2)
    listrow3 = Image.objects.filter(row=3)
    listrow4 = Image.objects.filter(row=4)

    context = {
        "name" : "Building",
        'objectlist' : queryset,       
        'row1' : listrow1,
        'row2' : listrow2,
        'row3' : listrow3,
        'row4' : listrow4,   
    }
    return render(request,"building.html", context)

def space_view(request):
    queryset = Image.objects.all().order_by('-id')
    listrow1 = Image.objects.filter(row=1)
    listrow2 = Image.objects.filter(row=2)
    listrow3 = Image.objects.filter(row=3)
    listrow4 = Image.objects.filter(row=4)

    context = {
        "name" : "Space",
        'objectlist' : queryset,       
        'row1' : listrow1,
        'row2' : listrow2,
        'row3' : listrow3,
        'row4' : listrow4,
    }
    return render(request, "space.html", context)

def nature_view(request):
    queryset = Image.objects.all().order_by('-id')
    listrow1 = Image.objects.filter(row=1)
    listrow2 = Image.objects.filter(row=2)
    listrow3 = Image.objects.filter(row=3)
    listrow4 = Image.objects.filter(row=4)

    context = {
        "name" : "Nature",
        'objectlist' : queryset,       
        'row1' : listrow1,
        'row2' : listrow2,
        'row3' : listrow3,
        'row4' : listrow4, 
    }
    return render(request, "nature.html", context)

def animasi_view(request):
    queryset = Image.objects.all().order_by('-id')
    listrow1 = Image.objects.filter(row=1)
    listrow2 = Image.objects.filter(row=2)
    listrow3 = Image.objects.filter(row=3)
    listrow4 = Image.objects.filter(row=4)

    context = {
        "name" : "Animasi",
        'objectlist' : queryset,       
        'row1' : listrow1,
        'row2' : listrow2,
        'row3' : listrow3,
        'row4' : listrow4, 
    }
    return render(request, "animasi.html", context)

def dynamic_image_view(request, my_id):
    obj = get_object_or_404(Image, id=my_id)
    queryset = Image.objects.all().order_by('-id')
    name = Image.objects.get(id=my_id)
    get_tag = Image.tags
    context = {
        "name" : "Post",
        "objects" : obj, 
        "tag"   : get_tag,
    }
    return render(request, "images.html", context)


def subtags_view(request, my_subtag):
 
    list = Image.objects.filter(subtags = my_subtag) 
    if my_subtag not in Image.tag():
        raise Http404
    context = {
        "name" : "subTags",
        "objects" : list, 
    }
    return render(request, "subtags.html", context)  

def about_view(request):
    context = {
        "name" : "About",
    }
    return render(request, "about.html", context)

def result_view(request):
    
    if request.method == "GET":
        search = request.GET['searched']
        result = Image.objects.filter(title__contains=search) or Image.objects.filter(tags__contains=search) or Image.objects.filter(caption__contains=search) or Image.objects.filter(subtags__contains=search)
        x = result.count()
        return render(request, "result.html", {'search' : search, 'name' : "Pencarian", 'result': result, 'number' : x})
    else:
        return render(request, "result.html", {'name' : "Pencarian"})    

