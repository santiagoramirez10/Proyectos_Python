# -*- coding: utf-8 -*-
"""
@author: Santiago Ramirez
"""
import os
directorio_actual=os.getcwd()
lista_archivos=os.listdir(directorio_actual)
numero_archivos=1
for i in lista_archivos:
    if i[-2:]!="py":
        print (str(numero_archivos)+"). "+i)
        numero_archivos+=1