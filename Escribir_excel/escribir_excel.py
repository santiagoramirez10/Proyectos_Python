# -*- coding: utf-8 -*-
"""
@author: Santiago Ramirez
"""
import xlsxwriter
nombre="Santiago"
apellido_1="Ramirez"
apellido_2="Pérez"
edad=25
pais="Colombia"
ciudad="Medellin"
datos=[nombre,apellido_1,apellido_2,edad,pais,ciudad]
archivo=xlsxwriter.Workbook('nombre.xlsx')
hoja=archivo.add_worksheet()
for i in range(len(datos)):
    hoja.write(0,i,datos[i])
archivo.close()