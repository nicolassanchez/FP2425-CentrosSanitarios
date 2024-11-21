# -*- coding: utf-8 -*-
"""
Created on Tue Oct 15 20:48:40 2019

@author: Toñi Reina
"""
from coordenadas import *

def test_calcular_media_coordenadas (coordenadas):
    '''Función para testear media_coordenadas

    @param coordenadas: Lista de tuplas de tipo Coordenada
    @type coordenadas: [Coordenada(float, float)]
    '''
    media = calcular_media_coordenadas(coordenadas)
    print (f'La media de las coordenadas de los centros es ({media[0]},{media[1]})')
     
def test_calcular_distancia (coordenada1, coordenada2):
    '''Función para testear calcular_distancia

    :param coordenada1: Una coordenada
    :type coordenada1: Coordenada(float, float)
    :param coordenada2: Una segunda coordenada
    :type coordenada2: Coordenada(float, float)
    '''
    dist = calcular_distancia(coordenada1, coordenada2)
    print (f'La distancia entre las coordenadas  {coordenada1} y {coordenada2} es {dist}')
   
def main():
    '''Función principal
    '''
    coordenada1= Coordenadas(36.52016726032299, -6.151330284937666)
    coordenada2= Coordenadas(36.67525095554243, -5.446052739188258)
    test_calcular_distancia(coordenada1, coordenada2)
    test_calcular_media_coordenadas([coordenada1, coordenada2])

if __name__=="__main__": 
    main()