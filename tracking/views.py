from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader

from .models import asset_catalog

# Create your views here.
def index(request):
    assets = asset_catalog.objects.all()
    template = loader.get_template('tracking/index.html')
    context = {
		'assets' : assets,
	}


    return HttpResponse(template.render(context, request))


def search(request):
    assets = asset_catalog.objects.all()
    template = loader.get_template('tracking/search.html')
    context = {
		'assets' : assets,
	}


    return HttpResponse(template.render(context, request))

def create(request):
    assets = asset_catalog.objects.all()
    template = loader.get_template('tracking/create.html')
    context = {
		'assets' : assets,
	}


    return HttpResponse(template.render(context, request))

def detail(request, asset_catalog_id):
    asset = asset_catalog.objects.get(id=asset_catalog_id)
    template = loader.get_template('tracking/details.html')
    print(asset)
    context = {
		'asset' : asset,
	}


    return HttpResponse(template.render(context, request))

def data(request):
    assets = asset_catalog.objects.all()
    template = loader.get_template('tracking/data.html')
    context = {
		'assets' : assets,
	}

    print(assets)


    return HttpResponse(template.render(context, request))

def store(request):

    asset = asset_catalog()
    asset.location = request.POST['location']
    asset.organization_tag = request.POST['tag']
    asset.manufacturer_part_num = request.POST['part']
    asset.manufacturer = request.POST['manufacturer']
    asset.description = request.POST['description']
    asset.date_implemented = request.POST['date']
    asset.maintenance_notes = request.POST['notes']

    asset.save()

    return HttpResponseRedirect('/tracking/data');

def update(request, asset_catalog_id):

    asset = asset_catalog.objects.get(id=asset_catalog_id)

    asset.location = request.POST['location']
    asset.organization_tag = request.POST['tag']
    asset.manufacturer_part_num = request.POST['part']
    asset.manufacturer = request.POST['manufacturer']
    asset.description = request.POST['description']
    asset.date_implemented = request.POST['date']
    asset.maintenance_notes = request.POST['notes']

    asset.save()

    return HttpResponseRedirect('/tracking/data');