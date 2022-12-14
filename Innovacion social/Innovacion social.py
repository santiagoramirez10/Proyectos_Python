# -*- coding: utf-8 -*-
"""
@author: Santiago Ramírez Pérez
"""
import random as rd
import xlsxwriter
import sqlite3
class Entradas():
    def __init__(self):
        self.vari = {"Localidades": 0, "Zonas": 0,
                     "Residencias": 0, "Escuelas": 0, "Escuelas": 0}
        for i in self.vari:
            while 1:
                entrada = input("Ingrese número de {}: ".format(i))
                try:
                    entrada = int(entrada)
                    self.vari[i] = entrada
                    while int(entrada) < 0:
                        entrada = input("Ingrese número de {}: ".format(i))
                    break
                except:
                    print("Ingrese un número válido, por favor")
    def vuelta(self):
        return (self.vari) 
class Localidades():
    def __init__(self,n_localidades):
        self.n_localidades=n_localidades 
    def Localidades_ICK(self):
        id_localidades=[]
        localidad_a=0
        while localidad_a<self.n_localidades:
            localidad=rd.randint(1,200)
            if localidad not in id_localidades:
                id_localidades.append(localidad)
                localidad_a+=1
        paso=int(200/(int(self.n_localidades**0.5)+1))-1
        direcciones=[]
        direccion_1=1
        direccion_2=direccion_1+paso
        localidad_a=0 
        while direccion_2<200:
            direcciones.append([direccion_1,direccion_2])
            direccion_1+=paso
            direccion_2+=paso
            localidad_a+=1
        calles=[]
        carreras=[]
        for j in range(len(direcciones)):
            for i in range(len(direcciones)):
                calles.append(direcciones[i])
                carreras.append(direcciones[j])
        calles=calles[:self.n_localidades]
        carreras=carreras[:self.n_localidades]
        return(id_localidades,calles,carreras)
class Zonas():
    def __init__(self,n_zonas):
        self.n_zonas=n_zonas 
    def Zonas_ICKF(self):
        id_zonas=[]
        zona_a=0
        while zona_a<self.n_zonas*n_localidades:
            zona=rd.randint(1,200)
            if zona not in id_zonas:
                id_zonas.append(zona)
                zona_a+=1
        calles_zonas=[]
        carreras_zonas=[]
        for k in range(n_localidades):
            direcciones=[]
            limite_1=calles_localidades[k][0]
            limite_2=calles_localidades[k][1]
            paso=int((limite_2-limite_1)/(int(self.n_zonas**0.5)+1))-1
            direccion_1=limite_1
            direccion_2=limite_1+paso
            localidad_a=0 
            while direccion_2<limite_2:
                direcciones.append([direccion_1,direccion_2])
                direccion_1+=paso
                direccion_2+=paso
                localidad_a+=1
            calles=[]
            carreras=[]
            for j in range(len(direcciones)):
                for i in range(len(direcciones)):
                    calles.append(direcciones[i])
                    carreras.append(direcciones[j])
            calles_zonas.append(calles[:self.n_zonas])
            carreras_zonas.append(carreras[:self.n_zonas])
        riesgos_zonas=[]
        for h in range(n_localidades):
            riesgos=[]
            for i in range(n_zonas):
                factores_riesgo=["P","M","PR","HC","HS","GAML","N"]
                riesgo_zona=[]
                presencia_riesgos=rd.randint(0,10)
                if presencia_riesgos<2:
                    riesgo_zona.append("N")
                else:
                    numero_riesgos=rd.randint(0,6)
                    for i in range(numero_riesgos):
                        riesgo=factores_riesgo[rd.randint(0,numero_riesgos)]
                        if riesgo not in riesgo_zona:
                            riesgo_zona.append(riesgo)
                if riesgo_zona==[]:
                    riesgo_zona.append("N")
                if "N" in riesgo_zona:
                    riesgo_zona=["N"]
                riesgos.append(riesgo_zona)
            riesgos_zonas.append(riesgos)
        return(id_zonas,calles_zonas,carreras_zonas,riesgos_zonas)
class Residencias():
    def __init__(self,n_residencias):
        self.n_residencias=n_residencias 
    def Residencias_ICK(self):
        id_residencias=[]
        residencia_a=0
        while residencia_a<self.n_residencias*n_zonas*n_localidades:
            residencia=rd.randint(1,500)
            if residencia not in id_residencias:
                id_residencias.append(residencia)
                residencia_a+=1
        direccion_a=0      
        direccion_localidades=[]    
        for i in range(n_localidades):
            direccion_zonas=[]
            for j in range(n_zonas):
                direccion_residencia=[]    
                for k in range(self.n_residencias):
                    calle_carrera=rd.randint(0,1)
                    if calle_carrera==0:
                        direccion="Calle "
                        direccion+=str(rd.randint(calles_zonas[i][j][0],calles_zonas[i][j][1]))
                        direccion+="#"+str(rd.randint(carreras_zonas[i][j][0],carreras_zonas[i][j][1]))
                        direccion+="-"+str(id_residencias[direccion_a])
                    if calle_carrera==1:
                        direccion="Carrera "
                        direccion+=str(rd.randint(carreras_zonas[i][j][0],carreras_zonas[i][j][1]))
                        direccion+="#"+str(rd.randint(calles_zonas[i][j][0],calles_zonas[i][j][1]))
                        direccion+="-"+str(id_residencias[direccion_a])
                    direccion_residencia.append(direccion)
                    direccion_a+=1
                direccion_zonas.append(direccion_residencia)
            direccion_localidades.append(direccion_zonas)
        return(id_residencias,direccion_localidades)
class Escuelas():
    def __init__(self,n_escuelas):
        self.n_escuelas=n_escuelas
    def Escuelas_ICK(self):
        id_escuelas=[]
        escuela_a=0
        while escuela_a<n_escuelas*n_zonas*n_localidades:
            escuela=rd.randint(1,500)
            if escuela not in id_escuelas:
                id_escuelas.append(escuela)
                escuela_a+=1
        direccion_a=0      
        direccion_localidades=[]    
        for i in range(n_localidades):
            direccion_zonas=[]
            for j in range(n_zonas):
                direccion_escuela=[]    
                for k in range(n_escuelas):
                    calle_carrera=rd.randint(0,1)
                    if calle_carrera==0:
                        direccion="Calle "
                        direccion+=str(rd.randint(calles_zonas[i][j][0],calles_zonas[i][j][1]))
                        direccion+="#"+str(rd.randint(carreras_zonas[i][j][0],carreras_zonas[i][j][1]))
                        direccion+="-"+str(id_residencias[direccion_a])
                    if calle_carrera==1:
                        direccion="Carrera "
                        direccion+=str(rd.randint(carreras_zonas[i][j][0],carreras_zonas[i][j][1]))
                        direccion+="#"+str(rd.randint(calles_zonas[i][j][0],calles_zonas[i][j][1]))
                        direccion+="-"+str(id_residencias[direccion_a])
                    direccion_escuela.append(direccion)
                    direccion_a+=1
                direccion_zonas.append(direccion_escuela)
            direccion_localidades.append(direccion_zonas)
        direcciones=[]
        for i in direccion_localidades:
            for j in i:
                for k in j:
                    direcciones.append(k)              
        return(id_escuelas,direcciones)   
class Estudiantes():
    def __init__(self):
        self.n_estudiantes=n_localidades*n_zonas*n_residencias
    def Estudiantes_ESGEJADRP(self):
        datos_estudiantes=[] 
        for i in range(self.n_estudiantes):
            Edad=rd.randint(0,25)
            Sexo=["Masculino","Femenino"][rd.randint(0,1)]
            Genero=["H","L","G","B","T","I","Q"][rd.randint(0,6)]
            Etnia=["Si", "No"][rd.randint(0,1)]
            JornadaE=["Mañana", "Tarde","Noche"][rd.randint(0,2)]
            Ausencia=rd.randint(0, 100)
            Disciplina=["D","F","A","O"][rd.randint(0,3)]
            RelacionesI=["D","F","A","O"][rd.randint(0,3)]
            PresenciaP=["D","F","A","O"][rd.randint(0,3)]
            datos_estudiantes.append([Edad,Sexo,Genero,Etnia,JornadaE,Ausencia,Disciplina,RelacionesI,PresenciaP])
        return(datos_estudiantes)    
#Datos iniciales
n_localidades=3          
n_zonas=5
n_residencias=15
n_escuelas=5
#Localidades
datos_localidades=Localidades(n_localidades).Localidades_ICK()
id_localidades=datos_localidades[0]
calles_localidades=datos_localidades[1]
carreras_localidades=datos_localidades[2]
#Zonas
datos_zonas=Zonas(n_zonas).Zonas_ICKF()
id_zonas=datos_zonas[0]
calles_zonas=datos_zonas[1]
carreras_zonas=datos_zonas[2]
riesgos_zonas=datos_zonas[3]
#Residencias
datos_residencias=Residencias(n_residencias).Residencias_ICK()
id_residencias=datos_residencias[0]
direcciones_residencias=datos_residencias[1]
#Escuelas
datos_escuelas=Escuelas(n_escuelas).Escuelas_ICK()
id_escuelas=datos_escuelas[0]
direcciones_escuelas=datos_escuelas[1]
#Estudiantes
datos_estudiantes=Estudiantes().Estudiantes_ESGEJADRP()
workbook  = xlsxwriter.Workbook("Innovacion social.xlsx")
worksheet = workbook.add_worksheet()
cabecera=["ID Localidad","Calles Localidad","Carreras Localidad","ID Zona",
          "Calles Zona","Carreras Zona","Factores de riesgo","ID Residencia",
          "Dirección Residencia","ID Escuela","Dirección Escuela","Edad","Sexo",
          "Género","Etnia","JornadaE","Ausencia","Disciplina",
          "RelacionesI","PresenciaP"]
for m in range(len(cabecera)):
    worksheet.write(0,m,cabecera[m])
fila=1
zona=0
for i in range(n_localidades):
    for j in range(n_zonas):
        for k in range(n_residencias):
            worksheet.write(fila,0,id_localidades[i])
            worksheet.write(fila,1,"Calles entre "+str(calles_localidades[i]))
            worksheet.write(fila,2,"Carreras entre "+str(carreras_localidades[i]))
            worksheet.write(fila,3,id_zonas[zona])
            worksheet.write(fila,4,"Calles entre "+str(calles_zonas[i][j]))
            worksheet.write(fila,5,"Carreras entre "+str(carreras_zonas[i][j]))
            worksheet.write(fila,6,",".join(riesgos_zonas[i][j]))
            worksheet.write(fila,7,id_residencias[fila-1])
            worksheet.write(fila,8,direcciones_residencias[i][j][k])
            escuela_aleatoria=rd.randint(0, len(id_escuelas)-1)
            worksheet.write(fila,9,id_escuelas[escuela_aleatoria])
            worksheet.write(fila,10,direcciones_escuelas[escuela_aleatoria])
            for l in range(len(datos_estudiantes[fila-1])):
                worksheet.write(fila,l+11,datos_estudiantes[fila-1][l])
            fila+=1
        zona+=1
workbook.close()  
conexion=sqlite3.connect('Innovacion social.db')
cursor=conexion.cursor()
cursor.execute('''CREATE TABLE Reto(ID_Localidad text,Calles_Localidad text,
                Carreras_Localidad text,ID_Zona number,Calles_Zona text,
                Carreras_Zona text,Factores_riesgo text,ID_Residencia number,
                Dirección_Residencia text,ID_Escuela number,Dirección_Escuela text,
                Edad number,Sexo text,Género text,Etnia text,JornadaE text,
                Ausencia number,Disciplina text,RelacionesI text,PresenciaP text)''')
fila=1
zona=0
for i in range(n_localidades):
    for j in range(n_zonas):
        for k in range(n_residencias):
            datos=datos_estudiantes[fila-1]
            Edad=datos[0]
            Sexo=datos[1]
            Genero=datos[2]
            Etnia=datos[3]
            JornadaE=datos[4]
            Ausencia=datos[5]
            Disciplina=datos[6]
            RelacionesI=datos[7]
            PresenciaP=datos[8]
            worksheet.write(fila,l+11,datos_estudiantes[fila-1][l])      
            escuela_aleatoria=rd.randint(0, len(id_escuelas)-1)
            instruccion=f"""INSERT INTO Reto VALUES({id_localidades[i]},
            '{"Calles entre "+str(calles_localidades[i])}',
            '{"Carreras entre "+str(carreras_localidades[i])}',
            {id_zonas[zona]},
            '{"Calles entre "+str(calles_zonas[i][j])}',
            '{"Carreras entre "+str(carreras_zonas[i][j])}',
            '{",".join(riesgos_zonas[i][j])}',
            {id_residencias[fila-1]},
            '{direcciones_residencias[i][j][k]}',
            {id_escuelas[escuela_aleatoria]},
            '{direcciones_escuelas[escuela_aleatoria]}',
            {Edad},
            '{Sexo}',
            '{Genero}',
            '{Etnia}',
            '{JornadaE}',
            {Ausencia},
            '{Disciplina}',
            '{RelacionesI}',
            '{PresenciaP}')"""
            cursor.execute(instruccion)
            conexion.commit() 
            fila+=1
        zona+=1
conexion.close()