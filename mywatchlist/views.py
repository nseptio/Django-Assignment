from django.shortcuts import render
from mywatchlist.models import BarangMywatchlist
from django.http import HttpResponse
from django.core import serializers

# Create your views here.

def show_mywatchlist(request):

    data_barang_mywatchlist = BarangMywatchlist.objects.all()
    context = {
        'list_barang': data_barang_mywatchlist,
        'nama': 'Septio Nugroho'
    }
    
    return render(request, "mywatchlist.html", context)

def show_mywatchlist_xml(request):
    data = BarangMywatchlist.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_mywatchlist_json(request):
    data = BarangMywatchlist.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_mywatchlist_json_by_id(request, id):
    data = BarangMywatchlist.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_mywatchlist_xml_by_id(request, id):
    data = BarangMywatchlist.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

