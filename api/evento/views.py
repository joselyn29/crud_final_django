from django.shortcuts import render
# importar JsonResponse
from django.http import JsonResponse
#importar los modelos en models.py 
from evento.models import evento_tbl

from django.views.decorators.csrf import csrf_exempt

# Create your views here.


#Función mostrar los datos existentes en la base de datos 

def select(request):
    evento = list(evento_tbl.objects.all().values())
    return JsonResponse(evento, safe=False)

@csrf_exempt
def insert(request):
    if request.method == 'POST':
        evento_tbl.objects.create(
            organizador = request.POST.get('organizador'),
            tipo = request.POST.get('tipo'),
            fecha = request.POST.get('fecha'),
            hora = request.POST.get('hora'),
            lugar = request.POST.get('lugar'),
            presupuesto = request.POST.get('presupuesto'),
            cantidad_personas=request.POST.get('cantidad')
        )
        data = {'info': "el usuario se ha ingresado correctamente"}
        return JsonResponse(data,safe=False)
    
    return JsonResponse({"nada":"nada"})

@csrf_exempt
def delete(request):
    if request.method == 'POST':
         evento_tbl.objects.filter(id=request.POST.get('id')).delete()
         data = {'info': "el usuario se ha eliminado correctamente"}
         return JsonResponse(data,safe=False)


    return JsonResponse({"nada":"nada"})


@csrf_exempt
def detalle_evento(request, evento_id):
        # Obtener el gasto específico por su ID
        eve = list(evento_tbl.objects.filter(id=evento_id).all().values())

        if eve == []:
            return JsonResponse({'error': 'El gasto no existe'}, status=404)
        else:
            return JsonResponse(eve, safe=False)

@csrf_exempt
def update(request):
    if request.method == 'POST':
        evento_id = request.POST.get('id')
        evento = evento_tbl.objects.filter(id=evento_id).first()

        if evento:
            # Verificar si alguno de los datos está vacío
            organizador = request.POST.get('organizador')
            tipo = request.POST.get('tipo')
            fecha = request.POST.get('fecha')
            hora = request.POST.get('hora')
            lugar = request.POST.get('lugar')
            presupuesto = request.POST.get('presupuesto')
            cantidad_personas = request.POST.get('cantidad_personas')

            # Verificar si algún campo está vacío
            if not all([organizador, tipo, fecha, hora, lugar, presupuesto, cantidad_personas]):
                # Si algún campo está vacío, puedes manejarlo según tus necesidades,
                # por ejemplo, mostrar un mensaje de error o redireccionar a otra página
             return JsonResponse({'error':'error'}, status=500)

            # Actualizar los campos con los datos que llegan de la web
            evento.organizador = organizador
            evento.tipo = tipo
            evento.fecha = fecha
            evento.hora = hora
            evento.lugar = lugar
            evento.presupuesto = presupuesto
            evento.cantidad_personas = cantidad_personas
            evento.save()

            # Mostrar mensaje de éxito

            # Redireccionar a la página de inicio (home)
            return JsonResponse({'exito':'exito'})

        # Si no se encuentra el evento, puedes devolver una respuesta de error o redireccionar a otra página
        return JsonResponse({'no se encontró el evento':'no se encontró el evento'})

    # Manejar el caso cuando no es una solicitud POST, posiblemente devolviendo una página de error
    return JsonResponse({'no es metodo post':'no es metodo post'})
