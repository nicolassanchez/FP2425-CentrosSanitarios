'''
Módulo para gestionar los centros sanitarios
Created on Tue Oct 15 20:48:20 2019

@author: Toñi Reina
'''
from typing import Iterable
from centros import *
from coordenadas import *

def mostrar_numerados(iterable: Iterable, n: int = 5) -> None:
    '''Función auxiliar que muestra por la consola una iterable de elementos.
    Cada elemento se muestra en una linea, con un ordinal que lo precede 

    @param iterable: iterable
    @type iterable: Iterable
    '''
    for n,e in enumerate(iterable):
        print (n,"-", e)
        if n == 5:
            break

def mostrar_centros(centros: list) -> None:
    '''Función de testeo de leer centros

    @param centros: Lista de tuplas de tipo CentroSanitario
    @type centros: [CentroSanitario(str, str, Coordenada(float, float), str, int, bool, bool)]
    '''
    print (f'\nSe han leido {len(centros)} centros:')
    mostrar_numerados(centros)
    
def test_calcular_total_camas_centros_accesibles(centros: list) -> None:
    '''Función de testeo de calcular_total_camas_centros_accesibles

    @param centros: Lista de tuplas de tipo CentroSanitario
    @type centros: [CentroSanitario(str, str, Coordenada(float, float), str, int, bool, bool)]
    '''
    
    total_camas_accesibles = calcular_total_camas_centros_accesibles(centros)
    print('\nEl numero total de camas de los centros accesibles es:', total_camas_accesibles)
    
def test_obtener_centros_con_uci_cercanos_a(centros: list, coordenada: Coordenadas, umbral: float) -> None:
    '''Función de testeo de obtener_centros_con_uci_cercanos_a

    @param centros: Lista de tuplas de tipo CentroSanitario
    @type centros: [CentroSanitario(str, str, Coordenada(float, float), str, int, bool, bool)]
    @param coordenada: tupla de tipo Coordenada con la latitud y logitud del punto 
    @type coordenada: Coordenada(float, float) 
    @param umbral: distancia máxima a la que deben estar los centros, marca el radio de distancia desde la coordenada
    @type umbral: float
    '''
    print (f'\nLos centros cercanos a las coordenadas ({coordenada.latitud},{coordenada.longitud}) son:')
    
    cercanos = obtener_centros_con_uci_cercanos_a(centros, coordenada, umbral)
    mostrar_numerados(cercanos)
    
    seguir: str = input("\nMostrar mapa en el navegador (S/N):")
    
    if seguir.upper() == "S": 
        generar_mapa(cercanos, "LAB-Centros-sanitarios-soluciones/out/mapa_centros_cercanos.html")    
    else:
        print ("\nNO SE MOSTRARAN LOS MAPAS")

def main() -> None:
    '''Función principal
    '''
    datos: list = leer_centros('LAB-Centros-sanitarios-soluciones/data/centrosSanitarios.csv')
    mostrar_centros(datos)
    
    test_calcular_total_camas_centros_accesibles(datos)
    print (f"\nEl número de centros por estado son: {obtener_total_centros_porEstado(datos)}")
    
    latitud1: float  = 36.52016726032299 
    longitud1: float = -6.151330284937666
    c1: Coordenadas = Coordenadas(latitud1, longitud1)
    
    latitud2: float  = 36.42016726032299 
    longitud2: float = -6.051330284937666
    c2: Coordenadas = Coordenadas(latitud2, longitud2)
    
    print(f"\nLa distancia entre {c1} y {c2} es: {calcular_distancia(c1,c2)}")
    
    test_obtener_centros_con_uci_cercanos_a(datos, c1, 0.75)    
    test_obtener_centros_con_uci_cercanos_a(datos, c2, 0.75)    
    
if __name__=="__main__":   
    main()