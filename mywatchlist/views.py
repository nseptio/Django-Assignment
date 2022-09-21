from django.shortcuts import render
from mywatchlist.models import MyWatchListtItem
from django.http import HttpResponse
from django.core import serializers

# Create your views here.

def show_mywatchlist(request):

    data_mywatchlist = MyWatchListtItem.objects.all()
    
    watched_counter = 0
    for item in data_mywatchlist:
        if item.watched:
            watched_counter += 1
    
    context = {
        'list_anime': data_mywatchlist,
        'nama': 'Septio Nugroho',
        'npm': '2106750843',
        'banyak_tonton': watched_counter >= (len(data_mywatchlist) - watched_counter),
    }
    return render(request, "mywatchlist.html", context)

def show_mywatchlist_xml(request):
    data = MyWatchListtItem.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_mywatchlist_json(request):
    data = MyWatchListtItem.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_mywatchlist_json_by_id(request, id):
    data = MyWatchListtItem.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_mywatchlist_xml_by_id(request, id):
    data = MyWatchListtItem.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

