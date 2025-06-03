from django.shortcuts import render
from .nasa_api import get_mars_photos

def mars_photos_view(request):
    earth_date = request.GET.get('date', '2020-07-01')  # Puedes cambiar la fecha base
    photos = get_mars_photos(earth_date)
    return render(request, "nasa_app/base.html", {'photos': photos, 'date': earth_date})
