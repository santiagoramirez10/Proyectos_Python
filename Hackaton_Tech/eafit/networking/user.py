from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import User, post
import json

@csrf_exempt
def task_list(request):
    if request.method == 'GET':
        tasks = User.objects.all()
        data = [{'id': User.id} for user in User]
        return JsonResponse({'user': data})
"""
    elif request.method == 'POST':
        data = json.loads(request.body)
        task_text = data.get('task_text', '')
        if task_text:
            task = Task(task_text=task_text)
            task.save()
            return JsonResponse({'task_text': task.task_text, 'id': task.id}, status=201)
        else:
            return JsonResponse({'error': 'La tarea debe tener una descripción'}, status=400)

@csrf_exempt
def task_detail(request, task_id):
    task = get_object_or_404(Task, pk=task_id)

    if request.method == 'DELETE':
        task.delete()
        return JsonResponse({'result': True})

"""