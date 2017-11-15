#!/usr/bin/env python
# -*- coding: utf-8 -*-
def ano(fecha):
	if fecha % 400 == 0 or (fecha % 100 != 0 and fecha % 4 == 0):
		print"El año", fecha, "es un año bisiesto."
	else:
		print"El año", fecha, "no es un año bisiesto."
print"Comprobador de años bisiestos"
fecha = int(input("Escriba un año y le diré si es bisiesto: "))
ano(fecha)
