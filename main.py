# -*- coding: utf-8 -*-
"""
Created on Mon Aug 15 12:14:33 2022

@author: Oscar Lesmes
"""
import math
c1 = (1,1)
c2 = (1,1)
def sumaComplejos(numero1, numero2):
    res = ()
    sumaReal = numero1[0] + numero2[0]
    sumaImaginaria = numero1[1] + numero2[1]
    res = (sumaReal, sumaImaginaria)
    return (res)

def restaComplejos(numero1, numero2):
    res = ()
    restaReal = numero1[0] - numero2[0]
    restaImaginaria = numero1[1] - numero2[1]
    res = (restaReal, restaImaginaria)
    return (res)

def multiplicacionComplejos(numero1, numero2):
    res = ()
    res = ((numero1[0]*numero2[0])-(numero1[1]*numero2[1]), (numero1[0]*numero2[1])+(numero2[0]*numero1[1]))
    return (res)

def divisionComplejos(numero1, numero2):
    res = ()
    denominador = (numero2[0]**2) + (numero2[1]**2)
    numeradorReal = (numero1[0]*numero2[0]) + (numero1[1]*numero2[1])
    numeradorImaginario = (numero2[0]*numero1[1]) - (numero1[0]*numero2[1])
    res = ((numeradorReal/denominador), (numeradorImaginario/denominador))
    return (res)

def moduloComplejo(numero1):
    modulo = math.sqrt((numero1[0]**2) + (numero1[1]**2))
    return (modulo)

def conjugadoComplejo(numero1):
    conjugadoImaginario = numero1[1] * -1
    res = (numero1[0], conjugadoImaginario)
    return (res)

def rectangular_polar(numero1):
    p = math.sqrt((numero1[0]**2) + (numero1[1]**2))
    teta = math.atan2(numero1[1], numero1[0])
    polar = (p, teta)
    return (polar)

def polar_rectangular(numero1):
    a = numero1[0]*math.cos(numero1[1])
    b = numero1[0]*math.sin(numero1[1])
    cartesiana = (a, b)
    return (cartesiana)

def faseComplejo(numero1):
    teta = math.atan2(numero1[1], numero1[0])
    return teta

def prettyprinting(c):
    print(str(c[0]) + "+" + str(c[1]) + "i")

prettyprinting(polar_rectangular(c1))
prettyprinting(rectangular_polar(c1))
