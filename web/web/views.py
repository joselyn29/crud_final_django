from django.shortcuts import render, redirect 
from django.http import JsonResponse
import requests


def Home(request):
    solicitud=requests.get('http://127.0.0.1:8001/Api/select/') 
    data = solicitud.json()
    return render(request,"home.html", {'data':data})

def crear(request):
    return render(request,"Insert.html", {})



def Select(request):
    
    solicitud=requests.get('http://127.0.0.1:8001/Api/select/') 
    data = solicitud.json()
    return JsonResponse(data, safe=False)

def Insert(request):
    if request.method == 'POST':
        # Obtener los datos del formulario
         organizador = request.POST.get('organizador')
         tipo = request.POST.get('tipo')
         fecha = request.POST.get('fecha')
         hora = request.POST.get('hora')
         lugar = request.POST.get('lugar')
         presupuesto = request.POST.get('presupuesto')
         cantidad_personas = request.POST.get('cantidad')

        # Crea un diccionario con los datos del formulario
         objecto = {
            'organizador': organizador,
            'tipo': tipo,
            'fecha': fecha,
            'hora': hora,
            'lugar':lugar,
            'presupuesto':presupuesto,
            'cantidad':cantidad_personas
        }

        # Realizar una solicitud POST para crear un nuevo registro en la API
         response = requests.post('http://127.0.0.1:8001/Api/insert/', data=objecto)
        
        # Verificar el código de estado de la respuesta
         if response.status_code == 200:
            # La creación fue exitosa
            mensaje = "Registro creado"
            return render(request, "Insert.html", {'mensaje':mensaje})
         else:
            # La creación no fue exitosa, manejar el error
            return JsonResponse({'error': 'No se pudo crear el registro en la API'}, status=500)
    else:
     return JsonResponse({'error': 'Solicitud no válida'}, status=400)
      # Si la solicitud no es POST, retornar un error
      

def Delete(request):
    if request.method == 'POST':
        # Obtener los datos del formulario
         id = request.POST.get('evento_id')
        # Crea un diccionario con los datos del formulario
         objeto = {
            'id': id,
        }

        # Realizar una solicitud POST para crear un nuevo registro en la API
         response = requests.post('http://127.0.0.1:8001/Api/delete/', data=objeto)
         solicitud=requests.get('http://127.0.0.1:8001/Api/select/') 

        
        # Verificar el código de estado de la respuesta
         if response.status_code == 200:
            # La creación fue exitosa
            mensaje = "Registro eliminado"
            data = solicitud.json()

            
            return render(request, "home.html", {'mensaje':mensaje, "data":data})
         else:
            # La creación no fue exitosa, manejar el error
            return JsonResponse({'error': 'No se pudo eliminar el registro en la API'}, status=500)
    else:
     return JsonResponse({'error': 'Solicitud no válida'}, status=400)
      # Si la solicitud no es POST, retornar un error
      

def actualizar_evento(request):
    if request.method == 'POST':
        # Obtener los datos del formulario
        id=request.POST.get('evento_id')
        organizador = request.POST.get('organizador')
        tipo = request.POST.get('tipo')
        fecha = request.POST.get('fecha')
        hora = request.POST.get('hora')
        lugar = request.POST.get('lugar')
        presupuesto = request.POST.get('presupuesto')
        cantidad_personas=request.POST.get('cantidad')

        # Crea un diccionario con los datos del formulario
        datos_eve = {
            'id':id,
            'organizador': organizador,
            'tipo': tipo,
            'fecha': fecha,
            'hora': hora,
            'lugar': lugar,
            'presupuesto': presupuesto,
            'cantidad_personas': cantidad_personas
        }
                
        # Realizar una solicitud a la API para actualizar el evento
        response = requests.post('http://127.0.0.1:8001/Api/update/', data=datos_eve)
        
        if response.status_code == 200:
            # Si la actualización fue exitosa, mostrar un mensaje de éxito
            mensaje = "Registro actualizado"
            dato = response.json()
            return render(request, "update.html", {"dato":dato, 'mensaje':mensaje})
        else:
            # Si no se pudo actualizar, devolver un mensaje de error
           mensaje_error="Inserta todos los datos a actualizar"
           return render(request, "update.html", {'mensaje_error':mensaje_error})
    else:
        # Manejar otros métodos de solicitud (GET, PUT, etc.) 
        return JsonResponse({'error': 'Solo POST'}, status=405)
    
def detalles(request, evento_id):

   # Realizar una solicitud a la API para obtener los detalles del evento
    evento_id = request.POST.get('evento_id')
    response = requests.get(f'http://127.0.0.1:8001/Api/detalle/{evento_id}/')

    if response.status_code == 200:
        detalle_eve = response.json()
        # Pasar los detalles del gasto al contexto de la plantilla
        return render(request, 'update.html', {'detalle_eve': detalle_eve})
    else:
        # Manejar el caso en el que no se puedan obtener los detalles del evento
        mensaje = "no se pudieron obtener los detalles del evento"
        return render(request, 'update.html', {'detalle_eve': detalle_eve, 'mensaje':mensaje})