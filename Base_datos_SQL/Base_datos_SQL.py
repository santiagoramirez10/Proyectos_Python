# -*- coding: utf-8 -*-
"""
@author: Santiago Ramirez
"""
import sqlite3
conexion=sqlite3.connect('mis_datos.db')
cursor=conexion.cursor()
cursor.execute('''CREATE TABLE mis_datos(Nombre text,Primer_apellido text,
               Segundo_apellido text,Numero_documento number,Ciudad text)''')
cursor.execute('''INSERT INTO mis_datos VALUES('Santiago','Ramírez','Pérez',
               1234567890,'Medellín')''')
conexion.commit()
conexion.close()









