# -*- coding: utf-8 -*-
"""
@author: Santiago Ramirez
"""
import numpy as np 
def matidentidad(n):    
    try:
        identidad=[]
        for i in range(n):
            identidad.append(n*[0])
        for i in range(len(identidad)):
            identidad[i][i]=1
    except:
        pass
    return identidad
n=20
print("\n Sin usar librerías:\n") 
for i in (matidentidad(n)):
    print(i)
#Usando numpy   
print("\n Usando numpy:\n") 
print(np.identity(n))







