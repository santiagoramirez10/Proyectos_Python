# -*- coding: utf-8 -*-
"""
@author: Santiago Ramirez

Clase Matrix
Clase que modela las matrices y sus operaciones básicas.
Entradas:
    m: número de filas, int, cero por defecto.
    n: número de columnas, int, cero por defecto.
    matrix: lista de listas, lista, None por defecto.
    
Salidas:
    Objeto tipo "Matriz".
    - Si Matriz=None, se genera con m filas y n columnas con valores
      aleatorios enteros entre 1 y 99.
    - Si se da solo un argumento entero, m = n.
    - Si matrix=lista, se genera la matriz que se ingrese manualmente si es
      válida.
"""
import random as rd
def isMatriz(obj):
    """
    Retorna True si el objeto es tipo Matriz. De lo contrario retorna False.
    Parámetros:
        obj: objeto.
    """
    if obj.__class__.__name__=="Matrix":
        return True
    return False
class Matriz():
    def __init__(self,m=0,n=0,matrix=None):
        """
        Constructor.
        
        Recibe los argumentos y guarda los atributos del objeto tipo Matriz.
        
        Atributos:
            self.matrix: matriz generada, lista de listas.
            self.rows: número de filas, int.
            self.columns: número de columnas, int.
        """
        #Para matriz aleatoria
        if matrix == None:
            self.matrix = []
            self.rows = m
            for i in range(1,m+1):
                #Para n=m, genera matriz cuadrada
                if n == 0:
                    self.columns = m
                    row = []
                    for j in range(1,m+1):
                        row.append(rd.randint(1,99)) #Genera valores aleatorios
                    self.matrix.append(row)
                #Para n != m, número de filas y columnas específicadas
                else:
                    self.columns = n
                    row = []
                    for j in range(1,n+1):
                        row.append(rd.randint(1,99)) #Genera valores aleatorios
                    self.matrix.append(row)
        #Para matriz específicada
        if type(matrix) == list:
            #Comprueba que las listas de la lista sean de igual tamaño
            cond = 0
            for i in range(len(matrix)):
                if len(matrix[0]) == len(matrix[i]):
                    cond = 1+cond
            if cond == len(matrix):
                #Guarda los atributos
                self.matrix = matrix
                self.rows = len(matrix)
                self.columns = len(matrix[0])
            #Si la lista de listas no es válida para ser matriz
            else:
                print("Matriz no válida")
    def set_value(self,i,j,value):
        """
        Cambia el valor en la posición seleccionada de la matriz.
        Parámetros:
            i: fila, int.
            j: columna, int.
            value: valor que estára en la posición [i][j] de la matriz, float.
        """
        self.matrix[i-1][j-1] = value
    def get_value(self,i,j):
        """
        Retorna el valor en la posición seleccionada de la matriz.
        
        Parámetros:
            i: fila, int.
            j: columna, int.
        Salidas:
            valor en la posición [i][j] de la matriz, float.
        """
        return self.matrix[i-1][j-1] 
    def __str__(self):
        """
        Método para print.
        Salidas:
            Imprime la matriz, tal como se escribe en matemáticas.
        """
        texto = ""
        for i in range(self.rows):
            texto = texto+str(self.matrix[i])+"\n"
        return texto 
    def __repr__(self):
        """
        Método para representación en consola.
        Salidas:
            Muestra las dimensiones de la matriz, así:
                Matrix(m,n)
        """
        return "Matrix("+str(self.rows)+","+str(self.columns)+")"
    def get_rows(self):
        """
        Retorna el número de filas de la matriz.
        Salidas:
            Número de filas, int.
        """
        return self.rows  
    def get_columns(self):
        """
        Retorna el número de columnas de la matriz.
        Salidas:
            Número de columnas, int.
        """
        return self.columns
    def __add__(self,other):
        """
        Suma de matrices.
        Retorna la suma de dos matrices. Las matrices deben de tener tanto el
        mismo número de filas como de columnas.
        Parámetros:
            other: matriz que va a sumar, tipo Matrix. 
        Salidas:
            La suma de las dos matrices, tipo Matrix.
        """
        #Valida que sean tipo Matrix
        if isMatriz(self) and isMatriz(other):
            #Valida las dimensiones de las matrices
            if self.rows==other.rows and self.columns==other.columns:
                result = Matriz(self.rows,self.columns)
                for i in range(self.rows):
                    for j in range(self.columns):
                        result.set_value(i+1,j+1,self.matrix[i][j]+other.matrix[i][j])
                return result
            #Si las dimensiones no son correctas
            else:
                print("Suma entre dos matrices no válida")
        #Si other no es tipo Matrix
        else:
            print("Uno de los dos elementos no es matriz")
    def __sub__(self,other):
        """
        Resta de matrices.
        Retorna la resta de dos matrices. Las matrices deben de tener tanto el
        mismo número de filas como de columnas.
        
        Parámetros:
            other: matriz que va a restar, tipo Matrix.
        Salidas:
            La resta de las dos matrices, tipo Matrix.  
        """
        #Valida que sean tipo Matriz
        if isMatriz(self) and isMatriz(other):
            #Valida las dimensiones de las matrices
            if self.rows==other.rows and self.columns==other.columns:
                result = Matriz(self.rows,self.columns)
                for i in range(self.rows):
                    for j in range(self.columns):
                        result.set_value(i+1,j+1,self.matrix[i][j]-other.matrix[i][j])
                return result
            #Si las dimensiones no son correctas
            else:
                print("Resta entre dos matrices no válida")
        #Si other no es tipo Matrix
        else:
            print("Uno de los dos elementos no es matriz")    
    def __mul__(self,other):
        """
        Multiplicación de matrices.
        
        Retorna la multiplicación de dos matrices. El número de columnas de la
        primera matriz(self), debe ser igual al número de filas de la segunda
        (other).
        Parámetros:
            other: matriz que va a multplicar, tipo Matriz.
        Salidas:
            La multiplicación de las dos matrices, tipo Matriz.
        """
        #Valida que sean tipo Matriz
        if isMatriz(self) and isMatriz(other):
            #Valida las dimensiones de las matrices
            if self.columns==other.rows:
                result = Matriz(self.rows,other.columns) #Matriz aleatoria
                mat = [] #Lista de listas con el resultado
                for i in range(self.rows):
                    row = []
                    for j in range(other.columns):
                        suma = 0
                        for k in range(self.columns):
                            num = self.matrix[i][k]*other.matrix[k][j]
                            suma = suma+num
                        row.append(suma)
                    mat.append(row)
                #Cambia la Matriz aleatoria por el resultado
                for i in range(result.rows):
                    for j in range(result.columns):
                        result.set_value(i+1,j+1,mat[i][j])
                return result
            #Si las dimensiones no son correctas
            else:
                print("Producto entre dos matrices no válida")
        #Si other no es tipo Matriz
        else:
            print("Ingrese dos matrices válidas")
    def scalar_mult(self,valor):
        """
        Multiplicación por escalar.
        Retorna la multiplicación de la matriz por un escalar.
        Parámetros:
            valor: Escalar que va a multiplicar, float.
        Salidas:
            La multplicación de la matriz por el escalar. 
        """
        if type(valor) == int or type(valor) == float:
            result = Matriz(self.rows,self.columns)
            for i in range(self.rows):
                for j in range(self.columns):
                    result.set_value(i,j,valor*self.matrix[i-1][j-1])
            return result      
    def transpose(self):
        """
        Transpuesta de una matriz.
        Retorna la transpuesta de la matriz.
        Parámetros:
            Matriz(self): tipo Matriz.
        Salidas:
            Matriz transpuesta: tipo Matriz 
        """
        #Valida si es tipo Matriz
        if isMatriz(self):
            result = Matriz(self.columns,self.rows)
            for i in range(self.columns):
                for j in range(self.rows):
                    result.set_value(i,j,self.matrix[j-1][i-1])
            return result
        #Si no es tipo Matriz
        else:
            print("Ingrese matriz válida")  
    def identity(n):
        """
        Matriz identidad.
        Retorna una matriz identidad de dimensiones dependiendo del caso.
        CASO 1:
        Parámetro:
            n: matriz cuadrada, tipo Matriz
        Salida:
            Matriz identidad del número de filas y columnas de n, tipo Matriz.
        CASO 2:
        Parámetro:
            n: número de filas y columnas, int.
        Salida:
            Matriz identidad de n número de filas y columnas. 
        """
        #Valida si el parámetro es tipo Matriz
        if type(n) == Matriz:
            #Valida si es una matriz cuadrada
            if n.rows == n.columns:
                result = Matriz(n.rows)
                for i in range(n.rows):
                    for j in range(n.rows):
                        if i == j:
                            result.set_value(i,j,1)
                        else:
                            result.set_value(i,j,0)
                return result
            #Si no es cuadrada
            else:
                print("No es Matriz cuadrada")
        #Si el parámetro es int
        elif type(n) == int:
            result = Matriz(n)
            for i in range(n):
                for j in range(n):
                    if i == j:
                        result.set_value(i,j,1)
                    else:
                        result.set_value(i,j,0)
            return result
        #Si el parámetro no es válido
        else:
            print("Argumento debe ser matriz o entero")