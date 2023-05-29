from django.shortcuts import render
from Routes.models import Location
from time import sleep
from plyer import notification
# from django.core.mail import send_mail
# from django.conf import settings


# obtener rutas
routes = Location.objects.all()

# notificacion
def enviarnotificacion(mensaje):
    notification.notify(
        title = "Recordatorio",
        message = mensaje,
        timeout = 10
    )

def repetir(func, time, veces, mensaje):
    
    while time>0:
        func(mensaje)
        time-=1
        sleep(veces)

# Create your views here.

def notificications(request):

    if request.method == 'POST':

        
        message = f"""{request.POST['rutas']} """

        
        # repetir(enviarnotificacio,)
        
        return render(request, 'notifications.html',{
            'routes': routes
            })
    
    return render(request, 'notifications.html',{
            'routes': routes
            })



