from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic.base import View


class HelloWorld(View):
    def get(self,request):
        information={
            'name':'Santiago Ramírez Pérez',
            'years':26,
            'codes':['Python','Arduino','JavaScript','Java']
        }
        return render(request,'hello_world.html', context=information)
