from funciones_generales import crear_matriz
from classBoton import Boton
from classLetra import Letra

def crear_teclado (x: int, y: int, width: int, height: int) -> list:
    """
    Crea y devuelve una matriz de botones y letras que representan un teclado de juego.

    Args:
        x (int): La coordenada x inicial para el primer botón del teclado.
        y (int): La coordenada y inicial para el primer botón del teclado.
        width (int): El ancho de cada botón del teclado.
        height (int): La altura de cada botón del teclado.

    Returns:
        list: Una matriz de objetos Letra, representando un teclado organizado en filas y columnas.
    """
    posicion_inicial = x
    
    matriz_letras = crear_matriz (3, 9)
    abcedario = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"

    posicion = 0
    for i in range (len(matriz_letras)):
        x = posicion_inicial
        for j in range (len(matriz_letras[0])):
            letra = abcedario [posicion]

            path = rf"image\Abecedario\{letra}.PNG"
            path_colision = rf"image\Abecedario\{letra} highlight.PNG"
            path_correcto = rf"image\Abecedario\{letra} si.PNG"
            path_incorrecto = rf"image\Abecedario\{letra} no.PNG"

            boton =  Boton ((x,y), (width, height), path, path_colision)

            letra_boton = Letra (letra, boton, path_correcto, path_incorrecto)

            matriz_letras[i][j] = letra_boton

            x += width

            posicion += 1
        y += height

    return matriz_letras