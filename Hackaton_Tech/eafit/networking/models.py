import random as rd
from datetime import datetime
import string
import pandas as pd
import json
import sqlite3

nombres_hombres = ["Juan", "Carlos", "Luis", "Miguel", "Pedro", "Alejandro", "Fernando", "Andres", "Javier", "Roberto"]
nombres_mujeres = ["Maria", "Ana", "Laura", "Sofia", "Isabel", "Elena", "Patricia", "Luisa", "Carmen", "Lorena"]
nombres=[nombres_hombres,nombres_mujeres]
apellidos = ["Gonzalez", "Rodriguez", "Lopez", "Martinez", "Perez", "Fernandez", "Gomez", "Sanchez", "Diaz", "Torres", "Vargas", "Ramirez", "Hernandez", "Castro", "Ruiz", "Ortega", "Jimenez", "Morales", "Silva", "Mendoza"]
roles=["Estudiante","Egresado","Empleado","Administrador"]
bd=[]
bd_json=[]
for i in range(100):
    hombre_mujer=rd.randint(0, 1)
    nombre_escogido=rd.randint(0, 9)
    nombre=nombres[hombre_mujer][nombre_escogido]
    apellido1=apellidos[rd.randint(0, 19)]
    apellido2=apellidos[rd.randint(0, 19)]
    apellido=apellido1+" "+apellido2
    nombre_completo=nombre+" "+apellido
    correo=nombre+"."+apellido1+str(rd.randint(1, 30))+"@eafit.edu.co"
    correo=correo.lower()
    fecha_actual = datetime.now()
    dia_aleatorio=rd.randint(1,28)
    mes_aleatorio=rd.randint(1,12)
    anio_aleatorio=rd.randint(1935,2007)
    fecha_nacimiento=datetime(anio_aleatorio,mes_aleatorio,dia_aleatorio)
    diferencia_anios = fecha_actual - fecha_nacimiento
    edad=diferencia_anios.days//365
    rol=roles[rd.randint(0,3)]
    if edad<20:
        rol="Estudiante"
    contrasenia = ''.join(rd.choice(string.ascii_letters) for _ in range(10))
    num_aleatorio = ''.join(rd.choice('0123456789') for _ in range(9))
    celular = '3' + num_aleatorio
    celular=int(celular)
    primer_loggeo=True
    datos_usuario=[nombre_completo,correo,contrasenia,celular,primer_loggeo,edad,rol]
    bd.append(datos_usuario)
    bd_json.append({"rol":rol,
                    "name":nombre_completo,
                    "email": correo,
                    "phone":celular,
                    "age":edad})
with open("bd_json.json", 'w') as archivo_json:
    json.dump(bd_json, archivo_json, indent=4)
df = pd.DataFrame(bd)
df.columns = ["name","email","password","phone","first_login","edad","tipo"]
conn = sqlite3.connect('comunidad_eafit.db')
df.to_sql('comunidad', conn, if_exists='replace', index=False)
conn.close()
#Convertir json a pandas
with open('bd_json.json', 'r') as archivo_json:
    datos = pd.read_json(archivo_json)