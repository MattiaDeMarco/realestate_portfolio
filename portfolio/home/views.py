from django.shortcuts import render, redirect
from .models import *

# Create your views here.

def homepage(request):

    properties = Property.objects.all()

    context = { 'properties':properties }

    return render(request, 'index.html', context)


def gallery(request):

    city = request.GET.get('city')
    if city == None:
        photos = Photo.objects.all()
    else:
        photos = Photo.objects.filter(city__name = city)

    
    properties = Property.objects.all()
    context = { 'properties':properties, 'photos':photos }

    return render(request, 'gallery.html', context)


def property(request, pk):

    property = Property.objects.get(id=pk)
    photos = property.photo_set.all()
    
    context = { 'property':property, 'photos':photos }

    return render(request, 'property.html', context)


def viewPhotos(request,pk):

    photo = Photo.objects.get(id=pk)
    
    context = { 'photo':photo }
    return render(request, 'photo.html', context)

def test(request, pk):

    property = Property.objects.get(id=pk)
    photos = property.photo_set.all()
    
    context = { 'property':property, 'photos':photos }

    return render(request, 'test.html', context)

"""
def upload(request):

    properties = Property.objects.all()

    if request.method == 'POST':
        data = request.POST
        images = request.FILES.getlist('images')

        if data['city'] != 'none':
            city = Property.objects.get(id=data['city'])
        elif data['category_new'] != '' :
            city, created = Property.objects.get_or_create(name=data['city_new'])
        else: 
            city = None

        for image in images:
            photo = Photo.objects.create(
                city = city,
                description = data['description'],
                image = image,
            )

        return redirect('gallery')


    context = { 'properties':properties }

    return render(request, 'upload.html', context)
    
"""