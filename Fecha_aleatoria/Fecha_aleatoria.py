# -*- coding: utf-8 -*-
"""
@author: Santiago Ramirez
"""
import random as rd
from datetime import datetime

inicio = datetime(2020,1,1)
final =  datetime(2022,11,11)
random_date = inicio + (final - inicio) * rd.random()
dia=str(random_date.day)
mes=str(random_date.month)
anio=str(random_date.year)
hora=str(random_date.hour)
minuto=str(random_date.minute)
if len(hora)==1:
  hora="0"+hora
if len(minuto)==1:
  minuto="0"+minuto

print("Fecha: "+dia+"/"+mes+"/"+anio)
print("Hora: "+hora+":"+minuto)
