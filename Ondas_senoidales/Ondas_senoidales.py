# -*- coding: utf-8 -*-
"""
@author: Santiago Ramirez
"""
import math#importamos las librerias a utilizar
import matplotlib.pyplot as plt
import random as ran

def fasor1(frecuencia,amplitud,desfase,ciclos,muestreo):#se define la primera funcion
    pi=math.pi                                          #donde se devuelven las 2 listas
    T=1/frecuencia#definicion de variables para realizar la lista del tiempo
    f=frecuencia
    dt=1/muestreo
    t=[]#lista vacia donde se añadira el tiempo 
    a=0
    while a<(T*ciclos):#ciclo para añadir los tiempos sumando dt veces
        t.append(a)
        a+=dt
        
        
    ejex=[]#listas vacias para añadir los datos, x tiempo y la funcion Asen(wt+fi)
    ejey=[]
     
    a=int(amplitud)
    fi=((desfase*pi)/180)#pasamos el desfase a radianes
    w=float(f)*2*pi#frecuencia angular
    for i in range(len(t)):
        ejex.append(t[i])#se añaden los valores a ambas listas
        ejey.append(a*(math.sin(((t[i])*w)+fi)))
    
    return(ejex) ,(ejey)#la funcion retorna las 2 listas requeridas
    

def desfase(b,d,f):#funcion desfase donde b,d son listas en el eje y y f la frecuencia
    pico1=b[0]#vamos a encontrar el maximo valor de b
    for j in b:
        if j>pico1:
            pico1=j
        pos1=b.index(pico1)#retorna la posicion del maximo valor de b
        
    
    pico2=d[0]#vamos a encontrar el maximo valor de d
    for j in d:
        if j>pico2:
            pico2=j
        pos2=d.index(pico2)#retorna la posicion del maximo valor de d    
    
    resta=a[pos1]-a[pos2]#restamos los dos tiempos donde estan los maximos valores de b y d
    valor=resta*360*-1*f#convertimos esa diferencia de tiempo en grados
    if abs(valor)==0:
        valor=0
    
    while abs(valor)>180:#ciclo para evitar errores en el desfase
        if valor<0:# valor absoluto(desfase) tiene que ser menor o igual a 180°
            valor=valor+360
        elif valor>0:
            valor=valor-360
    return(valor)#retorna el desfase en grados, en el rango de abs(desfase) menor o
                #igual a 180°

def grafasor1(a,b,d):#funcion para graficar donde a es el tiempo(mismo para ambas
                     #señales) y b,d son las litas de los ejes y de las señales
    plt.plot(a,b,"b")#primera señal graficada en azul
    plt.plot(a,d,"k")#segunda señal graficada en negro
    f=frecuencia
    grados=desfase(b,d,f)#tomamos el desfase para graficarlo
    t=[a[0]]#el desfase se muestra desde el tiempo 0 hasta el desfase
    t.append(abs(grados/(f*360)))#convertir desfase a segundos
    A=[(max(b)+max(d))/2,(max(b)+max(d))/2]#ubicacion de la linea de desfase en el eje y
    plt.xlabel("tiempo (seg)")
    plt.ylabel("A*sen(wt+fi) (V)")
    plt.plot(t,A,"r")#se imprime el desfase
    plt.title("Ondas senoidales")#nombramos la señal
    plt.legend(["Onda senoidal 1","Onda senoidal 2","Desfase ="+str(grados)],loc="lower right")
    #en la linea anterior creamos la leyenda para los datos de la grafica

amplitud=-4
fase=50
frecuencia=60
ciclos=2
muestreo=1200*frecuencia
a,b=fasor1(frecuencia,amplitud,fase,ciclos,muestreo)#a,b corresponden a ejex y ejey    
amplitud=5
fase=-155
c,d=fasor1(frecuencia,amplitud,fase,ciclos,muestreo)#c,d corresponden a ejex y ejey    
grafasor1(a,b,d)#se grafican ambas señales, a es el tiempo, b y d son loz

print("el desfase es: "+str(desfase(b,d,frecuencia)))#imprime en pantalla el desfase entre las señales      
#debido a la organizacion, la comentada y la introduccion con ejemplos incluidos,
#el autor decide colocar todo el trabajo en el mismo archivo para su mejor comprension.          