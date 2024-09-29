import pygame, sys
from funciones_generales import play_sound
from classGamesSet import Game
from classComodin import Comodin
from pantallas import show_lose_screen, show_win_screen

def wait_for_key() -> None:
    """
    Espera a que se presione una tecla o se cierre la ventana de Pygame para continuar.

    Esta función entra en un bucle hasta que se detecte un evento de teclado o de salida.
    """
    waiting = True

    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                waiting = False

def cargar_victoria (screen, nivel: Game, bandera_10_segundos: bool, comodin_multiplicar_puntos: Comodin) -> None:
    """
    Carga la pantalla de victoria y realiza acciones específicas dependiendo de las condiciones.

    Args:
        screen (pygame.Surface): La superficie de la pantalla de juego.
        nivel (Game): El objeto del nivel actual del juego.
        bandera_10_segundos (bool): Indica si se activó la bandera de 10 segundos.
        comodin_multiplicar_puntos (Comodin): El objeto del comodín de multiplicar puntos.
    """
    play_sound(r"musica\sonidos\Respuesta Correcta.mp3", 0.03)
    show_win_screen (screen)
    wait_for_key ()

    if bandera_10_segundos == True:
        comodin_multiplicar_puntos.cambiar_estado()

    nivel.nuevo_nivel(60)

def cargar_derrota (screen, nivel: Game) -> None:
    """
    Carga la pantalla de derrota y realiza acciones específicas al perder el nivel (frenar la música actual, reproducir una nueva de derrota y esperar a que el usuario ingrese una tecla).

    Args:
        screen (pygame.Surface): La superficie de la pantalla de juego.
        nivel (Game): El objeto del nivel actual del juego.
    """
    show_lose_screen (screen, nivel)
    pygame.mixer.music.stop() 
    play_sound (r"musica\sonidos\Perdiste.mp3", 0.03)
    wait_for_key ()
    pygame.mixer.music.play(-1)

def resetear_teclado (matriz_letras: list) -> None:
    """
    Reinicia el estado del teclado (matriz de letras) marcando todas las letras como no utilizadas.

    Args:
        matriz_letras (list): La matriz de letras del teclado.
    """
    for i in range (len(matriz_letras)):
        for j in range (len(matriz_letras[0])):
            if (matriz_letras[i][j].get_utilizado() == True):
                matriz_letras[i][j].cambiar_estado()