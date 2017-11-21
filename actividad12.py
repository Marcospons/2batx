#!/usr/bin/env python
# -*- coding: utf-8
s=0
r=0
d=0
m=0
letra=0
resultado=0
def suma(a,b):
    resultado=a+b
    return "El resultado es:",resultado
def resta(a,b):
    resultado=a-b
    return "El resultado es:",resultado
def multiplicacion(a,b):
    resultado=a*b
    return "El resultado es:",resultado
def division(a,b):
    resultado=a/b
    return "El resultado es:",resultado

print "Introduzca la primera variable"
a=int(input())
print "Introduzca la segunda variable"
b=int(input())
while letra<>"Fin":
    if letra=="D":
        print division(a,b)
    if letra=="S":
        print suma(a,b)
    if letra=="M":
        print multiplicacion(a,b)
    if letra=="R":
        print resta(a,b)
    print "Introduzca una letra que sea en mayusculas: S,R,M,D; o si quieres acabar escribe Fin"
    letra=raw_input()
if letra=="Fin":
    print "Fin."
