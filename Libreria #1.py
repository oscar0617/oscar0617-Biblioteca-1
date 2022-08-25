# -*- coding: utf-8 -*-
"""
Created on Mon Aug 15 12:14:33 2022

@author: Oscar Lesmes
"""
import math

def sumaComplejos(numero1, numero2):    #1
    res = ()
    sumaReal = numero1[0] + numero2[0]
    sumaImaginaria = numero1[1] + numero2[1]
    res = (sumaReal, sumaImaginaria)
    return (res)

def restaComplejos(numero1, numero2):   #2
    res = ()
    restaReal = numero1[0] - numero2[0]
    restaImaginaria = numero1[1] - numero2[1]
    res = (restaReal, restaImaginaria)
    return (res)

def multiplicacionComplejos(numero1, numero2):      #3
    res = ()
    res = ((numero1[0]*numero2[0])-(numero1[1]*numero2[1]), (numero1[0]*numero2[1])+(numero2[0]*numero1[1]))
    return (res)

def divisionComplejos(numero1, numero2):        #4
    res = ()
    denominador = (numero2[0]**2) + (numero2[1]**2)
    numeradorReal = (numero1[0]*numero2[0]) + (numero1[1]*numero2[1])
    numeradorImaginario = (numero2[0]*numero1[1]) - (numero1[0]*numero2[1])
    res = (round((numeradorReal/denominador), 3), round((numeradorImaginario/denominador), 3))
    return (res)

def moduloComplejo(numero1):        #5
    modulo = math.sqrt((numero1[0]**2) + (numero1[1]**2))
    return round(modulo, 3)

def conjugadoComplejo(numero1):         #6
    conjugadoImaginario = numero1[1] * -1
    res = (numero1[0], conjugadoImaginario)
    return (res)

def rectangular_polar(numero1):             #7
    p = math.sqrt((numero1[0]**2) + (numero1[1]**2))
    teta = math.atan2(numero1[1], numero1[0])
    polar = (round(p,2), round(teta,2))
    return (polar)

def polar_rectangular(numero1):             #8
    a = numero1[0]*math.cos(numero1[1])
    b = numero1[0]*math.sin(numero1[1])
    cartesiana = (round(a,2), round(b,2))
    return (cartesiana)

def faseComplejo(numero1):                  #9
    teta = math.atan2(numero1[1], numero1[0])
    return round(teta, 4)

def prettyprinting(c):
    if type(c) == tuple:
        if c[1] < 0:
            print(str(c[0]) + str(c[1]) + "i")
        elif c[1] == 0:
            print(str(c[0]))
        else:
            print(str(c[0]) + "+" + str(c[1]) + "i")
    else:
        print(str(c))

def prettyPrintingPolar(c):
    if type(c) == tuple:
        print(str(c[0]) + "," + str(c[1]) + "θ")
    else:
        print(str(c) + " θ")

c1 = (1,-1)
c2 = (1,0)

prettyprinting(sumaComplejos(c1, c2))
prettyprinting(restaComplejos(c1, c2))
prettyprinting(multiplicacionComplejos(c1, c2))
prettyprinting(divisionComplejos(c1, c2))
prettyprinting(moduloComplejo(c1))
prettyprinting(conjugadoComplejo(c1))
prettyPrintingPolar(rectangular_polar(c1))
prettyprinting(polar_rectangular(c1))
prettyPrintingPolar(faseComplejo(c1))


