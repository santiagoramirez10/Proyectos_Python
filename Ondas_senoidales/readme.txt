Este es un programa que tiene como fin crear 3 funciones la primera tiene como
objetivo devolver 2 listas, una que será el tiempo t y otra lista que será la funcion
A*Sen(wt + fi) evaluada en cada uno de los tiempos de la lista t.Las entradas 
para esta funcion son: amplitud, frecuencia, desfase, numero de ciclos, frecuencia
de muestreo.(la funcion se llama fasor)

La otra funcion se encargara de hallary retornar el desfase entre 2 señales 
creadas a partir de la funcion nombrada anteriormente, sus argumentos de entrada 
seran ambas listas correspondientes al eje y de las dos señales involucradas y 
la frecuencia(ambasfrecuencias deben de ser iguales).(la funcion se llama desfase)

Por ultimo tenemos una funcion que grafica ambas señales y especifica en la grafica
el desfase, siendo este un poco mas grafico para mejor comprension.(la funcion se
llama grafasor)

Por ejemplo:
si colocamos fasor(50,1,90,2,1100) entonces retornará 2 listas, una que sera ejex
donde iran los tiempos y ejey que va a ser A*Sen(wt + fi) evaluada en cada tiempo
de t, donde 50 es la frecuencia(w/2pi),1 es la amplitud(maximo valor en y),90 el
desfase, 2 el numero de ciclos y 1100 es la frecuencia de muestreo donde se va a 
añadir un dato a la lista ejex cada 1/frecuencia de muestreo segundos.

si colocamos desfase(ejey1,ejey2,f) la funcion recogera el maximo valor de ejey1
y ejey2 para poder saber en donde estan sus maximos y hacer la resta de tiempos, 
al conocer en que posicion se encuentra cada maximo se puede conocer su coordenada
tambien en x y asi obtener un diferencial en terminos del tiempo, luego es solo 
saber que el desfase sera ese delta de tiempo multiplicado por la frecuencia f y
multiplicando a 2pi o 360 si se requiere el desfase en radianes o grados.

por ultimo grafasor recibe como argumentos las listas del ejex y del eje y de 2
funciones para realizar su grafica utilizando la libreria matplotlib y alli 
adentro utilizamos una funcion similar a desfase para graficar este en la pantalla.