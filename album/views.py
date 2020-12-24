from django.shortcuts import render

# Create your views here.
from album.models import Album


def album(request):
    rsAlbum = Album.objects.all()

    return render(request, "album_list.html", {
        "rsAlbum": rsAlbum
    })