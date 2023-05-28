from django.shortcuts import render
import folium
from .models import Location

# Create your views here.

def routes(request):
    # obtener todas las rutas
    routess = Location.objects.all()

    # define el mapa
    initialMap = folium.Map(location=[10.4016011,-75.4879117], zoom_start=13)

    for route in routess:
        coordinates = (route.latitude, route.length)
        folium.Marker(coordinates, popup= route.name).add_to(initialMap)
    
    return render(request, 'routes.html',{
        'map': initialMap._repr_html_(),
        'Routes': routess
    })

  
    






