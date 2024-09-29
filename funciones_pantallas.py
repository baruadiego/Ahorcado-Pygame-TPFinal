import pygame
from Colores import *
from Comodines import *
from classGamesSet import Game
from classText_box import Text_box
from funciones_generales import crear_matriz, bubble_sort

def convertir_lista (palabra: str) -> list:
    """
    Convierte una cadena de texto en una lista donde cada elemento es un caracter de la cadena.

    Args:
        palabra (str): La cadena de texto que se desea convertir en lista.

    Returns:
        list: Una lista donde cada elemento es un caracter de la cadena.
    """
    lista = []
    for letra in palabra:
        lista.append(letra)
    return lista

def justificar_letras(pantalla, letras, fuente, color, x, y, ancho_maximo) -> None:
    """
    Dibuja una lista de letras en la pantalla justificando su espacio horizontalmente.

    Args:
        pantalla (pygame.Surface): La superficie de la pantalla donde se dibujarán las letras.
        letras (str or list): La cadena de texto o lista de caracteres a dibujar.
        fuente (pygame.font.Font): La fuente a utilizar para dibujar las letras.
        color (tuple): El color en formato RGB (Red, Green, Blue) de las letras.
        x (int): La posición x inicial donde comenzará el dibujo.
        y (int): La posición y donde se dibujarán las letras.
        ancho_maximo (int): El ancho máximo permitido para justificar las letras.
    """
    if type(letras) == str:
        letras = convertir_lista (letras)

    linea = []
    ancho_linea = 0

    for letra in letras:
        linea.append(letra)
        ancho_linea += fuente.size(letra)[0]

    # Calcular el espacio extra necesario para justificar la línea
    espacio_total = ancho_maximo - ancho_linea
    espacio_entre_letras = int (espacio_total / (len(linea) - 1))

    # Dibujar palabras con espacios extra entre ellas
    x_actual = x
    for letra in linea:
        texto_superficie = fuente.render(letra, True, color)
        pantalla.blit(texto_superficie, (x_actual, y))
        x_actual += fuente.size(letra)[0] + espacio_entre_letras

def calcular_margen (palabra: str) -> tuple[int, int]:
    """
    Calcula la posición x y el ancho máximo basado en la longitud de una palabra.

    Args:
        palabra (str): La palabra de la cual se calculará el margen.

    Returns:
        tuple[int, int]: Una tupla con la posición x y el ancho máximo calculado.
    """
    pos_x = 340
    ancho_maximo = 10
    for i in range (len(palabra)):
        pos_x -=  25
        ancho_maximo += 50
        
        if pos_x == 140:
            break

    return pos_x, ancho_maximo

def transformar_a_matriz (lista: list, filas: int, columnas: int) -> list:
    """
    Transforma una lista de diccionarios en una matriz de tamaño específico.

    Args:
        lista (list): La lista de diccionarios que se desea transformar en matriz.
        filas (int): El número de filas de la matriz.
        columnas (int): El número de columnas de la matriz.

    Returns:
        list: Una matriz con los datos de la lista organizados según las filas y columnas especificadas.
    """
    matriz = crear_matriz (filas, columnas)

    if len(lista) < filas:
        repeticion = len(lista)
    else:
        repeticion = len (matriz)

    j = 0
    for i in range (repeticion):
        if len(lista) >= i:
            matriz [i][j] = lista [i]["nombre"]
            matriz [i][j+1] = lista [i]["puntaje"]

    return matriz

def blitear_total_jugadores_unicos (screen, path: str, x: int, y: int) -> None:
    """Dibuja en pantalla la cantidad de jugadores con nicknames únicos registrados

    Args:
        screen (_type_): La superficie de la pantalla donde se dibujará el texto
        path (str): La ruta del archivo JSON que contiene los nombres de los jugadores
        x (int): La posición x donde se dibujará el texto
        y (int): La posición y donde se dibujará el texto
    """
    lista_jugadores = parser_json (path, "jugadores")
    nombres = set(map(lambda x: x['nombre'], lista_jugadores))

    texto = f"JUGADORES UNICOS: {len(nombres)}"
    blitear_textos (screen, fuente(25), texto, x, y)

def blitear_scores (screen, path: str) -> None:
    """
    Dibuja en pantalla los puntajes de los jugadores ordenados y transformados en matriz.

    Args:
        screen (pygame.Surface): La superficie de la pantalla donde se dibujarán los puntajes.
        path (str): La ruta del archivo JSON que contiene los puntajes de los jugadores.
    """
    lista_jugadores = parser_json (path, "jugadores")

    bubble_sort (lista_jugadores, key = lambda lista_jugadores: lista_jugadores["puntaje"], descendente = True)
    matriz_jugadores = transformar_a_matriz (lista_jugadores, 10, 2)

    y = 245
    for i in range (len(matriz_jugadores)):
        x = 220
        for j in range (len(matriz_jugadores[0])):
            texto = matriz_jugadores[i][j]
            blitear_textos (screen, fuente(30), texto, x, y)
            x += 205
        y += 45

def blitear_imagen(screen, path, width, height, x, y) -> None:
    """
    Dibuja una imagen en pantalla en la posición especificada con el tamaño dado.

    Args:
        screen (pygame.Surface): La superficie de la pantalla donde se dibujará la imagen.
        path (str): La ruta del archivo de imagen que se desea dibujar.
        width (int): El ancho de la imagen después de ser escalada.
        height (int): La altura de la imagen después de ser escalada.
        x (int): La posición x donde se dibujará la imagen.
        y (int): La posición y donde se dibujará la imagen.
    """
    imagen_surface = pygame.image.load (path)
    imagen_surface = pygame.transform.scale (imagen_surface, (width, height))
    screen.blit (imagen_surface, (x,y))

def blitear_textbox(screen, caja_texto: Text_box, font) -> None:
    """
    Dibuja un cuadro de texto en pantalla con el texto actual y un borde alrededor.

    Args:
        screen (pygame.Surface): La superficie de la pantalla donde se dibujará el cuadro de texto.
        caja_texto (Text_box): El objeto de cuadro de texto que contiene el texto a dibujar.
        font (pygame.font.Font): La fuente utilizada para dibujar el texto.
    """
    texto = font.render(caja_texto.get_text(), True, NEGRO) #Renderiza el texto
    
    #Dibuja el cuadro de texto
    margen_x = int ((caja_texto.width - texto.get_width()) / 2)
    screen.blit(texto, (caja_texto.x + margen_x, caja_texto.y + 5))
    pygame.draw.rect(screen, caja_texto.get_color(), caja_texto.rect, 2)

def blitear_teclado (screen, matriz_letras: list) -> None:
    """
    Dibuja en pantalla una matriz de botones representando un teclado de letras.

    Args:
        screen (pygame.Surface): La superficie de la pantalla donde se dibujarán los botones del teclado.
        matriz_letras (list): La matriz de botones de letras que forman el teclado.
    """
    for i in range (len(matriz_letras)):
        for j in range (len(matriz_letras[0])):
            screen.blit(matriz_letras[i][j].get_boton().get_imagen_surface(), matriz_letras[i][j].get_boton().get_rect())

def blitear_textos(screen, font, texto: str, x, y) -> None:
    """
    Dibuja texto en pantalla en la posición especificada con la fuente y color dados.

    Args:
        screen (pygame.Surface): La superficie de la pantalla donde se dibujará el texto.
        font (pygame.font.Font): La fuente utilizada para dibujar el texto.
        texto (str): El texto que se desea dibujar.
        x (int): La posición x donde se dibujará el texto.
        y (int): La posición y donde se dibujará el texto.
    """
    if type (texto) != str:
        texto = str(texto)
    textos = font.render (texto, False, NEGRO)
    screen.blit (textos, (x, y))

def manejo_errores (nivel: Game) -> str: 
    """
    Devuelve la ruta de la imagen correspondiente al número de errores del nivel.

    Args:
        nivel (Game): El objeto del nivel del juego que contiene el número de errores.

    Returns:
        str: La ruta de la imagen del ahorcado según el número de errores.
    """
    match nivel.get_errores():
        case 1:
            path = r"image\elementos\Ahorcado\Ahorcado1.png"
        case 2:
            path = r"image\elementos\Ahorcado\Ahorcado2.png"
        case 3:
            path = r"image\elementos\Ahorcado\Ahorcado3.png"
        case 4:
            path = r"image\elementos\Ahorcado\Ahorcado4.png"
        case 5:
            path = r"image\elementos\Ahorcado\Ahorcado5.png"
        case 6:
            path = r"image\elementos\Ahorcado\Ahorcado6.png"
        case 7:
            path = r"image\elementos\Ahorcado\Ahorcado7.png"
        case 8:
            path = r"image\elementos\Ahorcado\Ahorcado8.png"

    return path