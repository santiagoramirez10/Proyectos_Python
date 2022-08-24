# -*- coding: utf-8 -*-
"""
Autores: SANATIAGO RAMIREZ PEREZ

Email:   santiago.ramirez10@udea.edu.co
       
Archivo: Ramirez_Santiago_Reto_1.py
Fecha: 2020-04-05

Objetivo:   Este trabajo tiene como objetivo general, desarrollar una clase que
permita visualizar y analizar señales discretas de medidas, aplicando represen-
tacion matricial por series de Fourier y series de potencia
"""

import numpy as np#se importa la libreria numpy para los sistemas de ecuaciones
import random as rand#se importa la libreria random para señales aleatorias
from PyQt5.uic import loadUiType#se importa loadUiType para la interfaz
import sys #se importa sys para el correcto funcionamiento de QT
from PyQt5 import QtWidgets#se importa QtWidgets para la parte interactiva de 
                            #la interfaz
from matplotlib.figure import Figure#se importa matplotlib para graficas
from matplotlib.backends.backend_qt5agg import (
    FigureCanvasQTAgg as FigureCanvas,
    NavigationToolbar2QT as NavigationToolbar)#se importa FigureCanvas para que 
                                              #la figura se muestre en interfaz

Ui_MainWindow, QMainWindow = loadUiType('Fourier_potencia.ui')#se abre el
                                                                    #archivo de 
                                                                    #qt 

class Main(QMainWindow, Ui_MainWindow):#se define la clase Main en la cual 
                                        #se desarrollara todo el objetivo
    def __init__(self, ):
        """	
    	La funcion __init__ es la funcion que se ejecuta una vez y es al inicio
        del programa, es la que se encarga de asignar los espacios designados 
        mediante Qt para las graficas de las diferentes señales, ademas de 
        separar el espacio para dichas graficas, se asigna cada uno de los 
        botones de la interfaz a una funcion, dicha funcion se encarga de
        graficar dependiendo de cual sea su caso, hay un boton para lectura de
        datos, otro para generar una senoidal aleatoria, otro para una señal
        cuadrada aleatoria, y por ultimo para una señal rampa aleatoria.
    		
    	Parametros:
    		No tiene parametros de entrada.
    
    	Salidas:
    		SALIDA1: Designa cada una de las funciones y variables iniciales
            que se muestran a continuacion.
	    """
        super(Main, self).__init__()#se define la clase madre Main
        self.setupUi(self)
        fig = Figure()#se colocan los parametros para colocar las graficas en su
                        #respectivo recuadro
        self.canvas = FigureCanvas(fig)
        self.Grafica.addWidget(self.canvas)
        self.canvas.draw()
        self.toolbar = NavigationToolbar(self.canvas, 
                self.mplwindow, coordinates=True)
        self.Grafica.addWidget(self.toolbar)
        self.canvas2 = FigureCanvas(fig)
        self.Grafica_2.addWidget(self.canvas2)
        self.canvas2.draw()
        self.toolbar2 = NavigationToolbar(self.canvas2, 
                self.mplwindow_2, coordinates=True)
        self.Grafica_2.addWidget(self.toolbar2)
        self.GRAFICAR1.clicked.connect(self.graficas)#se asigna a cada boton una
                                                     #funcion especifica
        self.GRAFICAR2.clicked.connect(self.senoidal)
        self.GRAFICAR3.clicked.connect(self.cuadrada)
        self.GRAFICAR4.clicked.connect(self.rampa)
    
    def lectura(self,archivo):
        """	
    	La funcion lectura se encarga de leer cualquiera de los 31 archivos 
        asignados para el procesamiento de las señales discretas, esta funcion
        separa cada una de las lineas del archivo en columnas, siendo 3 columnas
        para el primer archivo y 2 columnas para el resto, esta funcion tiene
        como argumento de entrada el archivo que se desea leer y tiene como 
        salida 3 listas, correspondientes a las 3 columnas, para el caso de los
        archivos que solo tengan 2 columnas, la tercera columna sera un array
        vacio.
    		
    	Parametros:
    		PARAMETRO1 : Archivo al cual se le desea hacer la lectura.
    
    	Salidas:
    		SALIDA1 : Array con los datos del tiempo. 
            SALIDA2 : Array con los datos del eje y1. 
            SALIDA3 : Array con los datos del eje y2.
	    """
        file=open(archivo,"r")#se define a file como el archivo a leer
        arc=[]#se crea una lista para añadir cada uno de las lineas del archivo
        if archivo=="Senal_prueba.txt":#ciclo especial para Senal_prueba.txt
            for line in file:
                arc.append(line.split(" "))
        
        elif archivo[-4:]==".txt":#se asegura que el archivo sea de tipo txt
            for line in file:#se separa cada una de las lineas en listas de 3
                            #elementos
                arc.append(line.split(";"))#se separan por ";"
        file.close()#se cierra el archivo
        T=[]#se crean listas vacias para cada una de las columnas del archivo
        s1=[]
        s2=[]
        for i in arc[1:]:#se añaden a las listas los respectivos valores
            if i[0]!='\n' and len(i)==3:#siendo para las 3 columnas
                T.append(float(i[0]))
                s1.append(float(i[1]))
                s2.append(float(i[2]))
            elif len(i)==2:#o para las 2 columnas
                T.append(float(i[0]))
                s1.append(float(i[1]))
                s2=[]        
        T=np.array(T)#se cambian las listas a arrays
        s1=np.array(s1)
        s2=np.array(s2)
        return T,s1,s2#se retornan los 3 arrays
    
    def limpiar(self,):
        """	
    	La funcion limpiar es la que se encarga de eliminar la grafica que se 
        encuentre en el espacio designado para estas, esta funcion es necesaria
        debido a que si no se realiza, las graficas se van a sobreponer y van 
        a crear confusiones para el usuario
    		
    	Parametros:
    		No tiene parametros de entrada.
    
    	Salidas:
    		SALIDA1 : Limpia el espacio designado para las graficas.
	    """
        self.Grafica.removeWidget(self.canvas)#se elimina la grafica de la 
                                               #izquierda
        self.canvas.close()
        self.Grafica.removeWidget(self.toolbar)
        self.toolbar.close()   
        self.Grafica_2.removeWidget(self.canvas2)#se elimina la grafica de la 
                                                #derecha
        self.canvas2.close()
        self.Grafica_2.removeWidget(self.toolbar2)
        self.toolbar2.close()     
      
    def graficas(self):
        """	
    	La funcion graficar se encarga de leer el archivo deseado por el usuario,
        resolver el sistema de ecuaciones sea mediante numpy o el metodo de Gauss-
        Seidel, representarlo por series de Fourier o de potencia, y ademas de 
        ello, muestra el error que se tiene entre la señal original y la hallada,
        tambien es la que se encarga de graficar la señal leida en el texto y 
        a su vez grafica 
    	Parametros:*Todos los parametros se deben seleccionar en la interfaz
        grafica*
    		PARAMETRO1 : Nombre del archivo que se desea leer.
            PARAMETRO2 : Columna que se desea graficar.
            PARAMETRO3 : Metodo de solucion del sistema de ecuaciones.
            PARAMETRO4 : Metodo de representacion por series(Fourier o potencia).
            PARAMETRO5 : Iteraciones para los terminos de la serie.
            PARAMETRO6 : Iteraciones para el metodo de Gauss-Seidel.
    
    	Salidas:
    		SALIDA1 : Grafica de la señal original.
            SALIDA2 : Grafica de la señal representada mediante la serie seleccionada.
            SALIDA3 : Calculo del error entre los datos originales y la serie.
	    """
        self.limpiar()#se limpian los espacios para las graficas
        self.arch = self.SENAL.currentText()+'.txt'#se toma el archivo de interes
        T,s1,s2=self.lectura(self.arch)#se llama a la funcion lectura
        self.columna = self.COLUMNA.currentText()#se toma la columna de interes
        if self.columna=="Columna 2":# se define col como la columna de interes 
            col=s2
        else:
            col=s1
        fig=Figure()#se comienza la grafica de la señal original
        sub_f=fig.add_subplot(111)
        sub_f.grid()
        sub_f.plot(T,col)#se grafica la señal original
        self.canvas = FigureCanvas(fig)
        self.Grafica.addWidget(self.canvas)
        self.canvas.draw()
        self.toolbar = NavigationToolbar(self.canvas, 
                self.mplwindow, coordinates=True)#se coloca la señal original en
                                                 #el espacio determinado
        self.Grafica.addWidget(self.toolbar)
        self.metodo = self.METODO.currentText()#metodo de solucion de interes
        if self.metodo=="Numpy":#se realiza la solucion del sistema por numpy
            y1=self.Numpy(T,s1,s2)
        elif self.metodo=="Gauss-Seidel":#se realiza la solucion del sistema 
                                         #por Gauss-Seidel
            y1=self.Gauss_Seidel(T,s1,s2)            
        fig2 = Figure()#se comienza la grafica de la señal por series
        sub_f = fig2.add_subplot(111)
        sub_f.plot(T,y1)#se grafica la señal por series
        sub_f.grid()
        self.canvas2 = FigureCanvas(fig2)
        self.Grafica_2.addWidget(self.canvas2)
        self.canvas2.draw()
        self.toolbar2 = NavigationToolbar(self.canvas2, 
                self.mplwindow_2, coordinates=True)#se coloca la señal por series
                                                 #en el espacio determinado
        self.Grafica_2.addWidget(self.toolbar2)
        error1=np.linalg.norm(col-y1)#se halla el error
        error="Error utilizando "+self.metodo+":\n"+str(error1)
        self.ERROR.setText(error)#se muestra el error en la interfaz
 
    def senoidal(self):
        """	
    	La funcion senoidal, crea una señal aleatoria con forma senoidal, a la 
        cual se le puede sacar la representacion por series de potencia y Fourier,
        ademas de ello, cada que se oprime el boton correspondienter a la senoidal,
        ella crea una señal diferente, dando asi un espacio para el analisis, 
        grafica la señal original, (aleatoria creada), y a partir de la seleccion
        que haga el usuario, se resuelve el sistema de ecuaciones por numpy o por
        Gauss-Seidel, se grafica mediante series de potencia o de Fourier y se 
        muestra el error correspondiente.
        
    	Parametros:*Todos los parametros se deben seleccionar en la interfaz
        grafica*
            PARAMETRO1 : Metodo de solucion del sistema de ecuaciones.
            PARAMETRO2 : Metodo de representacion por series(Fourier o potencia).
            PARAMETRO3 : Iteraciones para los terminos de la serie.
            PARAMETRO4 : Iteraciones para el metodo de Gauss-Seidel.
    
    	Salidas:
    		SALIDA1 : Grafica de la señal original.
            SALIDA2 : Grafica de la señal representada mediante la serie seleccionada.
            SALIDA3 : Calculo del error entre los datos originales y la serie.
	    """
        self.limpiar()#se limpian los espacios para las graficas
        A=rand.uniform(-20,20)#amplitud de la señal, aleatoria
        fi=rand.uniform(-np.pi,np.pi)#desfase de la señal, aleatorio
        p=rand.uniform(1,4)#periodo de la señal, aleatorio
        w=2*np.pi/p#frencuencia angular, depende del periodo
        T=np.arange(0,p,0.001)#array del tiempo
        s1=np.zeros_like(T)#se crea el array para el eje y
        for i in range(len(T)):#se añaden los datos al eje y
            s1[i]=(A*np.sin(w*T[i]+fi))
        s2=[]#segundo array del eje y como vacio
        fig=Figure()#se comienza la grafica de la señal original
        sub_f=fig.add_subplot(111)
        sub_f.grid()
        sub_f.plot(T,s1)#se grafica la señal original
        self.canvas = FigureCanvas(fig)
        self.Grafica.addWidget(self.canvas)
        self.canvas.draw()
        self.toolbar = NavigationToolbar(self.canvas, 
                self.mplwindow, coordinates=True)#se coloca la señal original en
                                                 #el espacio determinado
        self.Grafica.addWidget(self.toolbar)
        self.metodo = self.METODO.currentText()#metodo de solucion de interes
        if self.metodo=="Numpy":#se realiza la solucion del sistema por numpy
            y1=self.Numpy(T,s1,s2)
        elif self.metodo=="Gauss-Seidel":#se realiza la solucion del sistema 
                                         #por Gauss-Seidel
            y1=self.Gauss_Seidel(T,s1,s2)            
        fig2 = Figure()#se comienza la grafica de la señal por series
        sub_f = fig2.add_subplot(111)
        sub_f.plot(T,y1)#se grafica la señal por series
        sub_f.grid()
        self.canvas2 = FigureCanvas(fig2)
        self.Grafica_2.addWidget(self.canvas2)
        self.canvas2.draw()
        self.toolbar2 = NavigationToolbar(self.canvas2, 
                self.mplwindow_2, coordinates=True)#se coloca la señal por series
                                                 #en el espacio determinado
        self.Grafica_2.addWidget(self.toolbar2)
        error1=np.linalg.norm(s1-y1)#se halla el error
        error="Error utilizando "+self.metodo+":\n"+str(error1)
        self.ERROR.setText(error)#se muestra el error en la interfaz

    def cuadrada(self):
        """	
    	La funcion cuadrada, crea una señal aleatoria cuadrada, a la cual se le 
        puede sacar la representacion por series de potencia y Fourier,ademas 
        de ello, cada que se oprime el boton correspondienter a la cuadrada,
        ella crea una señal diferente, dando asi un espacio para el analisis, 
        grafica la señal original, (aleatoria creada), y a partir de la seleccion
        que haga el usuario, se resuelve el sistema de ecuaciones por numpy o por
        Gauss-Seidel, se grafica mediante series de potencia o de Fourier y se 
        muestra el error correspondiente.
        
    	Parametros:*Todos los parametros se deben seleccionar en la interfaz
        grafica*
            PARAMETRO1 : Metodo de solucion del sistema de ecuaciones.
            PARAMETRO2 : Metodo de representacion por series(Fourier o potencia).
            PARAMETRO3 : Iteraciones para los terminos de la serie.
            PARAMETRO4 : Iteraciones para el metodo de Gauss-Seidel.
    
    	Salidas:
    		SALIDA1 : Grafica de la señal original.
            SALIDA2 : Grafica de la señal representada mediante la serie seleccionada.
            SALIDA3 : Calculo del error entre los datos originales y la serie.
	    """
        self.limpiar()#se limpian los espacios para las graficas
        A=rand.uniform(0.1,20)#valor maximo en y para la señal, aleatorio
        t2=np.arange(-1,1.01,0.01)#array para el tiempo de la señal original
        u1=lambda t2: np.piecewise(t2,t2>=A,[A,0])#se crea la señal cuadrada
        u2=lambda t2: np.piecewise(t2,t2>=0,[A,0])
        col=u2(t2)-u1(t2)#se aasigna a col como los datos del eje y
        s2=[]#lista vacia del ejey2
        T=np.arange(0,2.01,0.01)#array para el tiempo
        fig=Figure()#se comienza la grafica de la señal original
        sub_f=fig.add_subplot(111)
        sub_f.grid()
        sub_f.plot(T,col)#se grafica la señal original
        self.canvas = FigureCanvas(fig)
        self.Grafica.addWidget(self.canvas)
        self.canvas.draw()
        self.toolbar = NavigationToolbar(self.canvas, 
                self.mplwindow, coordinates=True)#se coloca la señal original en
                                                 #el espacio determinado
        self.Grafica.addWidget(self.toolbar)
        self.metodo = self.METODO.currentText()#metodo de solucion de interes
        if self.metodo=="Numpy":#se realiza la solucion del sistema por numpy
            y1=self.Numpy(T,col,s2)
        elif self.metodo=="Gauss-Seidel":#se realiza la solucion del sistema 
                                         #por Gauss-Seidel
            y1=self.Gauss_Seidel(T,col,s2)            
        fig2 = Figure()#se comienza la grafica de la señal por series
        sub_f = fig2.add_subplot(111)
        sub_f.plot(T,y1)#se grafica la señal por series
        sub_f.grid()
        self.canvas2 = FigureCanvas(fig2)
        self.Grafica_2.addWidget(self.canvas2)
        self.canvas2.draw()
        self.toolbar2 = NavigationToolbar(self.canvas2, 
                self.mplwindow_2, coordinates=True)#se coloca la señal por series
                                                 #en el espacio determinado
        self.Grafica_2.addWidget(self.toolbar2)
        error1=np.linalg.norm(col-y1)#se halla el error
        error="Error utilizando "+self.metodo+":\n"+str(error1)
        self.ERROR.setText(error)#se muestra el error en la interfaz
              
    def rampa(self):
        """	
    	La funcion rampa, crea una señal rampa aleatoria, a la cual se le 
        puede sacar la representacion por series de potencia y Fourier,ademas 
        de ello, cada que se oprime el boton correspondienter a la rampa,
        ella crea una señal diferente, dando asi un espacio para el analisis, 
        grafica la señal original, (aleatoria creada), y a partir de la seleccion
        que haga el usuario, se resuelve el sistema de ecuaciones por numpy o por
        Gauss-Seidel, se grafica mediante series de potencia o de Fourier y se 
        muestra el error correspondiente.
        
    	Parametros:*Todos los parametros se deben seleccionar en la interfaz
        grafica*
            PARAMETRO1 : Metodo de solucion del sistema de ecuaciones.
            PARAMETRO2 : Metodo de representacion por series(Fourier o potencia).
            PARAMETRO3 : Iteraciones para los terminos de la serie.
            PARAMETRO4 : Iteraciones para el metodo de Gauss-Seidel.
    
    	Salidas:
    		SALIDA1 : Grafica de la señal original.
            SALIDA2 : Grafica de la señal representada mediante la serie seleccionada.
            SALIDA3 : Calculo del error entre los datos originales y la serie.
	    """
        self.limpiar()#se limpian los espacios para las graficas
        A=rand.uniform(0.1,20)#valor maximo del eje x, aleatorio
        t=np.arange(-1*A,A+0.01,0.01)#se crea la señal rampa origial
        u=(t>=0)*1
        col=t*u#datos en el eje y para la señal original
        s2=[]#lista vacia del ejey2
        T=np.arange(0,(2*A)+0.01,0.01)#array para el tiempo
        fig=Figure()#se comienza la grafica de la señal original
        sub_f=fig.add_subplot(111)
        sub_f.grid()
        sub_f.plot(T,col)#se grafica la señal original
        self.canvas = FigureCanvas(fig)
        self.Grafica.addWidget(self.canvas)
        self.canvas.draw()
        self.toolbar = NavigationToolbar(self.canvas, 
                self.mplwindow, coordinates=True)#se coloca la señal original en
                                                 #el espacio determinado
        self.Grafica.addWidget(self.toolbar)
        self.metodo = self.METODO.currentText()#metodo de solucion de interes
        if self.metodo=="Numpy":#se realiza la solucion del sistema por numpy
            y1=self.Numpy(T,col,s2)
        elif self.metodo=="Gauss-Seidel":#se realiza la solucion del sistema 
                                         #por Gauss-Seidel
            y1=self.Gauss_Seidel(T,col,s2)            
        fig2 = Figure()#se comienza la grafica de la señal por series
        sub_f = fig2.add_subplot(111)
        sub_f.plot(T,y1)#se grafica la señal por series
        sub_f.grid()
        self.canvas2 = FigureCanvas(fig2)
        self.Grafica_2.addWidget(self.canvas2)
        self.canvas2.draw()
        self.toolbar2 = NavigationToolbar(self.canvas2, 
                self.mplwindow_2, coordinates=True)#se coloca la señal por series
                                                 #en el espacio determinado
        self.Grafica_2.addWidget(self.toolbar2)
        error1=np.linalg.norm(col-y1)#se halla el error
        error="Error utilizando "+self.metodo+":\n"+str(error1)
        self.ERROR.setText(error)#se muestra el error en la interfaz
    
    def Numpy(self,T,s1,s2):
        """	
    	La funcion Numpy es la que se encarga de realizar la representacion de 
        las señales, sea por series de Fourier o por series de potencia, (segun 
        la preferencia del usuario), esta representacion la hace tomando como
        entrada las 3 listas de datos y realiza la solucion del sistema de 
        ecuaciones mediante la libreria numpy, para las series, hay un espacio
        en donde el usuario puede indicar el numero de iteraciones que desea 
        para el procedimiento.
        
    	Parametros:*Todos los parametros se deben seleccionar en la interfaz
        grafica*
            PARAMETRO1 : Metodo de solucion del sistema de ecuaciones.
            PARAMETRO2 : Metodo de representacion por series(Fourier o potencia).
            PARAMETRO3 : Iteraciones para los terminos de la serie de Fourier.
            PARAMETRO4 : Array con los datos en el eje del tiempo.
            PARAMETRO5 : Array con los datos en el ejey 1.
            PARAMETRO6 : Array con los datos en el ejey 2.
            PARAMETRO7 : Columna que se desea graficar.
            
    
    	Salidas:
    		SALIDA1 : Array con los datos en el eje y correspondientes a la sol
            del sistema de ecuaciones.
	    """
        self.columna = self.COLUMNA.currentText()#columna de interes
        self.serie=self.SERIE.currentText()#serie por la que se desea representar
        if self.columna=="Columna 2":#se define col como la columna de interes
            col=s2
        else:
            col=s1
        x=T#se define x como el array del tiempo
        n=int(self.ITERACIONES.text())#se toma el numero de iteraciones indicado 
                                      #para las series
        p=T[-1]#periodo de la funcion
        f=1/p#frecuencia de la funcion
        wo=2*np.pi*f#frecuencia angular de la funcion
        d=T[1]-T[0]#delta del tiempo
        if self.serie=="Fourier":#si la serie es la de Fourier, entonces:
            sist="Series de Fourier"#variable para indicar que serie es
            F_o=lambda x:((2/p)*sum(col)*d)+ 0*T#a0 de la serie de Fourier
            F_cos=lambda x,w,k:np.cos(k*w*x)#an de la serie de Fourier
            F_sin=lambda x,w,k:np.sin(k*w*x)#bn de la serie de Fourier
            L=[F_o(x)]#se asignan los a0 a la variable L
            for q in range(1,n+1):
                yan = F_cos(x,wo,q)#se añaden los an y bn a  la lista L
                ybn = F_sin(x,wo,q)
                L.append(yan)
                L.append(ybn)
            A=np.array(L)#A es un array de L
            B=A.T#B es la transpuesta de A
        elif self.serie=="Potencia":#si la serie es la de potencia, entonces:
            sist="Series de Potencia"#variable para indicar que serie es
            F_p = lambda T,n:np.power(T,n)#polinomio-n para la serie de potencia
            L = []#lista vacia para añadir los polinomios
            for q in range(n+1):#se añaden los polinomios a la lista L
                y = F_p(T,q)
                L.insert(0,y)
            A = np.array(L)#A es un array de L
            B = A.T#B es la transpuesta de A
        sol=np.linalg.solve(np.dot(B.T,B),np.dot(B.T,col))
        y1=np.dot(B,sol)#se soluciona el sistema de ecuaciones
        self.SISTEMA.setText(sist)#se muestra en la interfaz que serie es
        return y1#se retorna un array con los datos del eje y
    
    def Gauss_Seidel(self,T,s1,s2):
        """	
    	La funcion Gauss-Seidel es la que se encarga de realizar la representacion 
        de las señales, sea por series de Fourier o por series de potencia, (segun 
        la preferencia del usuario), esta representacion la hace tomando como
        entrada las 3 listas de datos y realiza la solucion del sistema de 
        ecuaciones mediante un metodo iterativo llamado Gauss-Seidel, 
        para las series, hay un espacio en donde el usuario puede indicar el 
        numero de iteraciones que desea para el procedimiento.
        
    	Parametros:*Todos los parametros se deben seleccionar en la interfaz
        grafica*
            PARAMETRO1 : Metodo de solucion del sistema de ecuaciones.
            PARAMETRO2 : Metodo de representacion por series(Fourier o potencia).
            PARAMETRO3 : Iteraciones para los terminos de la serie de Fourier.
            PARAMETRO4 : Array con los datos en el eje del tiempo.
            PARAMETRO5 : Array con los datos en el ejey 1.
            PARAMETRO6 : Array con los datos en el ejey 2.
            PARAMETRO7 : Columna que se desea graficar.
    
    	Salidas:
    		SALIDA1 : Array con los datos en el eje y correspondientes a la sol
            del sistema de ecuaciones.
	    """
        self.columna = self.COLUMNA.currentText()#columna de interes
        self.serie=self.SERIE.currentText()#serie por la que se desea representar
        if self.columna=="Columna 2":#se define col como la columna de interes
            col=s2
        else:
            col=s1
        x=T#se define x como el array del tiempo
        n=int(self.ITERACIONES.text())#se toma el numero de iteraciones indicado 
                                      #para las series
        p=T[-1]#periodo de la funcion
        f=1/p#frecuencia de la funcion
        wo=2*np.pi*f#frecuencia angular de la funcion
        if self.serie=="Fourier":#si la serie es la de Fourier, entonces:
            sist="Series de Fourier"#variable para indicar que serie es
            d=T[1]-T[0]
            F_o=lambda x:((2/p)*sum(col)*d)+ 0*T#a0 de la serie de Fourier
            F_cos=lambda x,w,k:np.cos(k*w*x)#an de la serie de Fourier
            F_sin=lambda x,w,k:np.sin(k*w*x)#bn de la serie de Fourier
            L=[F_o(x)]#se asignan los a0 a la variable L
            for q in range(1,n+1):
                yan = F_cos(x,wo,q)#se añaden los an y bn a  la lista L
                ybn = F_sin(x,wo,q)
                L.append(yan)
                L.append(ybn)
            A=np.array(L)#A es un array de L
            B=A.T#B es la transpuesta de A
        elif self.serie=="Potencia":#si la serie es la de potencia, entonces:
            sist="Series de Potencia"#variable para indicar que serie es
            F_p = lambda T,n:np.power(T,n)#polinomio-n para la serie de potencia
            L = []#lista vacia para añadir los polinomios
            for q in range(n+1):#se añaden los polinomios a la lista L
                y = F_p(T,q)
                L.insert(0,y)
            A = np.array(L)#A es un array de L
            B = A.T#B es la transpuesta de A
        C=np.dot(B.T,B)#se definen nuevas variables para el metodo de Gauss-Seidel
        D=np.dot(B.T,col)
        z=np.zeros_like(D)
        it=int(self.ITERACIONES_GS.text())#iteraciones para el metodo de Gauss
        for k in range(it):#estos son los pasos del algoritmo de Gauss-Seidel
            for i in range(len(D)):
                z[i]=(D[i]-np.sum(C[i][:i]*z[:i])
                -np.sum(C[i][i+1:]*z[i+1:]))/C[i][i]
        y2 = np.dot(B,z)#se soluciona el sistema de ecuaciones
        self.SISTEMA.setText(sist)#se muestra en la interfaz que serie es
        return y2#se retorna un array con los datos del eje y
     
if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    main = Main()#se inicia la clase 
    main.show()#se muestra la interfaz
    sys.exit(app.exec_()) 