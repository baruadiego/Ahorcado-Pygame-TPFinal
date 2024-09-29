import pygame
from classGamesSet import Game
from Colores import *
from abecedario import *
from funciones_pantallas import *
from funciones_generales import *

def show_menu_screen(screen, boton_menu: Boton, boton_menu_score: Boton) -> None:
    """
    Muestra la pantalla del menú principal del juego.

    Args:
        screen (pygame.Surface): La superficie de la pantalla de Pygame.
        boton_menu (Boton): Objeto Boton para el botón de jugar en el menú.
        boton_menu_score (Boton): Objeto Boton para el botón de puntajes en el menú.
    """
    #Fondo
    blitear_imagen(screen, r"image\Menu\Menu fondo.png", 700, 700, 0, 0)
    
    #Botones
    screen.blit(boton_menu.get_imagen_surface(), boton_menu.get_rect())
    screen.blit(boton_menu_score.get_imagen_surface(), boton_menu_score.get_rect())

    #Actualizamos pantalla
    pygame.display.update()

def show_scores_screen(screen, boton_return: Boton) -> None:
    """
    Muestra la pantalla de puntajes del juego.

    Args:
        screen (pygame.Surface): La superficie de la pantalla de Pygame.
        boton_return (Boton): Objeto Boton para el botón de retorno a menú en la pantalla de puntajes.
    """
    #Fondo
    blitear_imagen(screen, r"image\Fondos\fondo_scores.png", 700, 700, 0, 0)

    #Botones
    screen.blit(boton_return.get_imagen_surface(), boton_return.get_rect())
    
    blitear_total_jugadores_unicos (screen, r"json/jugadores.json", 240, 180)

    #Lista de puntajes
    blitear_scores(screen, r"json/jugadores.json")

    #Actualizamos pantalla
    pygame.display.update()

def show_game_screen(screen, nivel: Game, caja_texto: Text_box, comodin_tiempo_extra: Comodin,
                     comodin_revelar_letra: Comodin, comodin_multiplicar_puntos: Comodin,
                     matriz_letras: list) -> None:
    """
    Muestra la pantalla de juego principal.

    Args:
        screen (pygame.Surface): La superficie de la pantalla de Pygame.
        nivel (Game): Objeto Game que representa el estado del juego.
        caja_texto (Text_box): Objeto Text_box para la caja de texto donde se ingresa la letra.
        comodin_tiempo_extra (Comodin): Objeto Comodin para el comodín de tiempo extra.
        comodin_revelar_letra (Comodin): Objeto Comodin para el comodín de revelar letra.
        comodin_multiplicar_puntos (Comodin): Objeto Comodin para el comodín de multiplicar puntos.
        matriz_letras (list): Lista de objetos Boton representando el teclado de letras.
    """
    #Botones
    blitear_imagen(screen, r"image\Fondos\fondo_teclado.png", 700, 700, 0, 0)
    
    #Espacio para palabra central
    blitear_imagen(screen, r"image\Fondos\fondo_texto_central.png", 450, 85, 120, 440)
    
    #Epacio para temática
    blitear_imagen(screen, r"image\Fondos\fondo_texto_central.png", 350, 60, 180, 150)
    
    #Justificación de palabra central
    pos_x, ancho_maximo = calcular_margen(nivel.get_palabra())
    justificar_letras(screen, nivel.get_lista_aciertos(), fuente(55), NEGRO, pos_x, 460, ancho_maximo)
    
    #Justificación de temática
    justificar_letras(screen, nivel.get_categoria(), fuente(50), NEGRO, 190, 165, 330)

    #comodines
    screen.blit(comodin_tiempo_extra.get_boton().get_imagen_surface(), comodin_tiempo_extra.get_boton().get_rect())
    screen.blit(comodin_revelar_letra.get_boton().get_imagen_surface(), comodin_revelar_letra.get_boton().get_rect())
    screen.blit(comodin_multiplicar_puntos.get_boton().get_imagen_surface(), comodin_multiplicar_puntos.get_boton().get_rect())

    blitear_teclado(screen, matriz_letras)

    blitear_textbox(screen, caja_texto, fuente(80))


    #Foto central segun errores
    if nivel.get_errores() > 0:
        blitear_imagen(screen, manejo_errores(nivel), 400, 500, 160, 120)

    #tiempo
    if nivel.get_tiempo_restante() >= 0:
        tiempo = str(f"{nivel.get_tiempo_restante():.2f}")
    else:
        tiempo = "00:00"
    blitear_textos(screen, fuente(50), tiempo, 30, 90)

    #puntaje
    score = f"{nivel.get_puntaje()}"
    score = zfill_propio(score, 4)
    blitear_textos(screen, fuente(50), score, 589, 93)

    #actualizamos pantalla
    pygame.display.update()

def show_win_screen(screen) -> None:
    """
    Muestra la pantalla de victoria del juego.

    Args:
        screen (pygame.Surface): La superficie de la pantalla de Pygame.
    """
    blitear_imagen(screen, r"image\elementos\Indicadores\palabra_correcta.png", 600, 150, 50, 275)
    pygame.display.update()

def show_lose_screen(screen, nivel: Game) -> None:
    """
    Muestra la pantalla de derrota del juego.

    Args:
        screen (pygame.Surface): La superficie de la pantalla de Pygame.
        nivel (Game): Objeto Game que representa el estado del juego.
    """
    #fondo
    blitear_imagen(screen, r"image\Fondos\fondo_derrota.png", 700, 700, 0, 0)
    
    #espacio palabra central
    blitear_imagen(screen, r"image\Fondos\fondo_texto_central.png", 450, 85, 120, 440)

    #Palbra completa
    pos_x, ancho_maximo = calcular_margen(nivel.get_palabra())
    justificar_letras(screen, nivel.get_palabra(), fuente(60), NEGRO, pos_x, 460, ancho_maximo)

    #puntaje
    score = zfill_propio(str(nivel.get_puntaje()), 4)
    blitear_textos(screen, fuente(80), score, 285, 105)

    #Imagen ahorcado
    blitear_imagen(screen, r"image\elementos\Ahorcado\Ahorcado8.png", 400, 500, 160, 120)
    pygame.display.update()

def show_nickname_screen(screen, nickname_caja_texto: Text_box) -> None:
    """
    Muestra la pantalla para ingresar el nickname del jugador.

    Args:
        screen (pygame.Surface): La superficie de la pantalla de Pygame.
        nickname_caja_texto (Text_box): Objeto Text_box para la caja de texto donde se ingresa el nickname.
    """
    blitear_imagen(screen, r"image\Fondos\Ingrese Nombre.png", 700, 700, 0, 0)

    blitear_textbox(screen, nickname_caja_texto, fuente(80))
    pygame.display.update()
