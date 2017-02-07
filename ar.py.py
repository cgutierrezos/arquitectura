# -*- coding: utf-8 -*-

"""
Hacer un programa que calcule la multiplicación de dos enteros sin signo usando solo
sumas.
"""
def mult(a, b):
    if b==0 or a==0:
        return 0
    elif b==1:
        return a
    elif a==1:
        return b
    else:
        return a+mult(a,b-1)




"""
Realice un programa que calcule la potencia de dos números enteros sin signo
realizando llamados a la función desarrollada en el punto 1.
"""

def pot(a, b):
    if b==0:
        return 1
    elif b==1:
        return a
    else:
        return mult(a, pot(a, b-1))
    


"""
Realice un programa que calcule un polinomio de grado n, en donde los coeficientes
del polinomio se encuentran almacenados en un vector k de n+1 posiciones
"""

def pol(k, x, n):
    if n==0:
        if len(k)==1:
            return k.pop()
        else:
            return k.pop(0)+pol(k,x,n)
    else:
        return mult(k.pop(0), pot(x, n))+pol(k, x, n-1)
    
    

"""
Realice un programa que calcule el factorial de un número entero sin signo
"""


def fact(a):
    if a==1 or a==0:
        return 1
    else:
        return mult(a, fact(a-1))


"""
Realice un programa calcule la división entera entre dos números enteros
"""

def divent(a, b):
    if(a<b):
        return 0
    else:
        cont=0
        c=b
        while(b<=a):
            cont=cont + 1
            b=b+c
        return cont


"""
resultados
"""

n1=7
n2=3




print mult(n1, n2)
print pot(n1, n2)
print fact(n1)
print pol([2,3,2,2],2, 2)
print divent(20, 5)
