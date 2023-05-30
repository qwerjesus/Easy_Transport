from django.shortcuts import render
from Routes.models import Location
from time import sleep
from plyer import notification
# from django.core.mail import send_mail
# from django.conf import settings


# obtener rutas
routes = Location.objects.all()

# notificacion
def enviarnotificacion(mensaje, title):
    notification.notify(
        title = title,
        message = mensaje,
        timeout = 10
    )

def repetir(time, veces, titulo):
    s = 12
    a = 9
    wq = a/(s*(s-a)) #tiempo de espera
    cwq = wq*60
    count_time = 0
    total = time*veces
    while total>0:

        if cwq>time:
            t = cwq - count_time
            mensaje = f' falta aun {t} minutos para que llegue el bus de transcaribe en {titulo}'

            enviarnotificacion(mensaje, titulo)

            total-=time
            count_time=time
            sleep(time)
            continue
        else: break

# Create your views here.

def notificications(request):

    if request.method == 'POST':

        
        titulo = request.POST['rutas']
        tiempo = int(request.POST['time'])
        veces = int(request.POST['countTime'])

        
        repetir(tiempo, veces, titulo)
        
        return render(request, 'notifications.html',{
            'routes': routes
            })
    
    return render(request, 'notifications.html',{
            'routes': routes
            })


