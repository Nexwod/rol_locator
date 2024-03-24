from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import RolPoints
from django.db.models import Q

from .forms import RolForm, RolSearchForm


# Create your views here.
def home_view(request, *args, **kwargs):
    
    return render(request, "home.html", {})


def Rol_register_view(request, *args, **kwargs):
    form = RolForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = RolForm()

    context = {
        'form':form
    }
    return render(request, "Rol_register.html", context)

def Rol_register_update_view(request, id):
    obj = RolPoints.objects.get(id=id)
    form = RolForm(request.POST or None, instance = obj)
    if form.is_valid():
        form.save()
        return redirect(f"../../locator/details/{id}")

    context = {
        'form':form
    }
    return render(request, "Rol_register_update.html", context)




def all_points_view(request, *args, **kwargs):
    obj_list = RolPoints.objects.order_by('-id')

    context = {
        "RolPoints":obj_list
    }
    return render(request, "all_points.html", context)

def details_view(request, my_id):
    obj = get_object_or_404(RolPoints, id=my_id)
    context = {
        "RolPoints":obj
    }
    return render(request, "details.html", context)

def search_view(request, *args, **kwargs):
    # obj = get_object_or_404(RolPoints, id=my_id)
    # context = {
    #     "RolPoints":obj
    # }
    form = RolSearchForm()
    return render(request, "search.html", {'form':form})


def search_items_view(request):
    # query = request.GET["search"]
    # obj_list = RolPoints.objects.filter(Q(address__icontains=query))
    
    # context={
    #     "RolPoints":obj_list
    # }
    # return render(request, "search_items.html", {})
    if request.method == 'GET':
        form = RolSearchForm(request.GET)
        if form.is_valid():
            address = form.cleaned_data.get('address')
            co_ordinator = form.cleaned_data.get('co_ordinator')
            region = form.cleaned_data.get('region')
            results = RolPoints.objects.all()
            if address:
                results = results.filter(address__icontains=address)
            if region:
                results = results.filter(region__icontains=region)
            if co_ordinator:
                results = results.filter(co_ordinator__icontains=co_ordinator)
            return render(request, 'search_items.html', {'results': results, 'address': address, 'region': region, 'co_ordinator': co_ordinator})
    else:
            form = RolSearchForm()
    return render(request, 'search.html', {'form': form})