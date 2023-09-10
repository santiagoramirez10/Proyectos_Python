from django.shortcuts import render
from django.http import HttpResponse
import json
from django.http import JsonResponse
from django.views import View

def networking(request):
    return HttpResponse("Hello world!")
# Create your views here.


# views.py


class GetNameFromEmail(View):
    def get(self, request, email):
        # Lee el archivo JSON (asumiendo que está en la carpeta del proyecto)
        with open('bd_json.json', 'r') as json_file:
            data = json.load(json_file)

        # Busca el correo electrónico en los datos JSON
        name = None
        for item in data:
            if item.get('email') == email:
                name = item.get('name')
                break

        if name:
            # Devuelve el valor de 'name' en la respuesta JSON
            return JsonResponse({'name': name})
        else:
            # Si el correo electrónico no se encontró, puedes devolver un error 404 u otra respuesta adecuada.
            return JsonResponse({'error': 'Correo electrónico no encontrado'}, status=404)