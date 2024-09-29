import pygame, sys
from funciones_instancias_juego import *
from event_handler import *
from pantallas import *
from classGamesSet import Game
from classText_box import Text_box
from funciones_generales import *
from Comodines import *
from abecedario import crear_teclado

def run_menu (screen) -> None:
    """
    Ejecuta el bucle del menú del juego.

    Args:
        screen (pygame.Surface): La superficie de la pantalla donde se muestra el menú.
    """
    boton_menu =  Boton ((350,400), (350,270), r"image\Menu\Jugar inactivo.png", r"image\Menu\Jugar activo.png")
    boton_menu_score =  Boton ((350,610), (210,130), r"image\Scores\boton_score.png", r"image\Scores\boton_scores_activo.png")
    
    run = True
    scores = False
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEMOTION:
                event_mousemotion_menu (event, boton_menu, boton_menu_score)
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                run, scores = event_mousebuttondown_menu (event, run, scores, boton_menu, boton_menu_score)

        if scores == True:
            run_scores(screen)
            scores = False

        show_menu_screen (screen, boton_menu, boton_menu_score)

def run_scores (screen):
    """
    Ejecuta el bucle para mostrar los puntajes de los 10 mejores jugadores.

    Args:
        screen (pygame.Surface): La superficie de la pantalla donde se muestran los puntajes.
    """
    boton_return = Boton ((50,50), (75,60), r"image\Scores\boton_return.png", r"image\Scores\boton_return activo.png")
    
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEMOTION:
                event_mousemotion_scores (event, boton_return)
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                run = event_mousebuttondown_scores (event, run, boton_return)

        show_scores_screen (screen, boton_return)

def run_game (screen) -> int:
    """
    Ejecuta el bucle principal del juego.

    Args:
        screen (pygame.Surface): La superficie de la pantalla donde se muestra el juego.

    Returns:
        int: El puntaje obtenido al finalizar el juego.
    """
    #Instancias de objetos:

    #Comodines
    comodin_tiempo_extra, comodin_revelar_letra, comodin_multiplicar_puntos = instanciar_comodines (230, 85, 120, 100)
    
    matriz_letras = crear_teclado (140, 550, 50, 50)

    #Caja de texto
    char_width, char_height = fuente(80).size ("w")
    caja_texto = Text_box (600, 450, char_width+10, char_height+3, ROJO, NEGRO)
    caja_texto.set_estado (True)

    #Nivel
    nivel = Game (60, 8, 0)
    nivel.iniciar_nivel()

    #Bucle del juego
    run = True
    while run:
        pygame.time.set_timer (pygame.USEREVENT, 10000)
        bandera_10_segundos = False
        
        #Bucle del nivel
        while nivel.get_nivel_terminado() == False:
            if nivel.get_tiempo_restante() < 0:
                nivel.terminar_nivel()
    
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.MOUSEMOTION:
                    event_mousemotion_game (event, caja_texto, comodin_tiempo_extra, comodin_revelar_letra, comodin_multiplicar_puntos, matriz_letras)
                elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    event_mousebuttondown_game (event, nivel,comodin_tiempo_extra, comodin_revelar_letra, comodin_multiplicar_puntos, matriz_letras)
                elif event.type == pygame.KEYDOWN:
                    event_keydown_game (event, nivel, caja_texto, matriz_letras)
                elif event.type == pygame.USEREVENT:
                    bandera_10_segundos = event_time_game (bandera_10_segundos,comodin_multiplicar_puntos)

            show_game_screen (screen, nivel, caja_texto, comodin_tiempo_extra, comodin_revelar_letra, comodin_multiplicar_puntos, matriz_letras)

        pygame.mouse.set_system_cursor (pygame.SYSTEM_CURSOR_ARROW)
        if nivel.get_victoria() == True:
            cargar_victoria (screen, nivel, bandera_10_segundos, comodin_multiplicar_puntos)
        else:
            cargar_derrota (screen, nivel)
            run = False
            
        resetear_teclado(matriz_letras)
    
    return nivel.get_puntaje()

def run_nickname (screen) -> str:
    """
    Ejecuta el bucle para ingresar y validar un nickname.

    Args:
        screen (pygame.Surface): La superficie de la pantalla donde se ingresa el nickname.

    Returns:
        str: El nickname ingresado y validado.
    """
    pygame.mouse.set_system_cursor (pygame.SYSTEM_CURSOR_IBEAM)
    char_width, char_height = fuente(80).size ("WWWWW")
    nickname_caja_texto = Text_box (213, 520, char_width+10, char_height+3, ROJO, NEGRO)
    nickname_caja_texto.set_estado (True)

    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                run = event_keydown_nickname (event, nickname_caja_texto, run)

        show_nickname_screen (screen, nickname_caja_texto)

    return nickname_caja_texto.get_text()