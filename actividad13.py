# -*- coding: utf-8 -*-
def crealista(lista):
    numeros = int(input("Cuantos numeros quieres?"))
    if numeros < 0:
        print "IMPOSIBLE"
    else:
        for i in range (numeros):
            num = int(input("Introduce un numero:"))
            lista+= [num]
        print lista


def sumalista(lista):
    suma = 0
    for i in lista:
        suma+=i
    print suma
numero = 0
lista = []
crealista(lista)
sumalista(lista)
