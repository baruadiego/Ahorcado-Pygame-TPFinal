import pygame
from instancias_juego import *
from settings_music import play_music
from funciones_generales import guardar_juego

def main():
    """
    Función principal que ejecuta el juego del AHORCADO.

    Inicializa la ventana de Pygame, ejecuta el menú principal, el juego, la pantalla para ingresar el nickname,
    y guarda el puntaje del jugador en un archivo JSON.
    """
    SCREEN_WIDTH = 700
    SCREEN_HEIGHT = 700
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("AHORCADO GAME")

    pygame.init()
    play_music(r"musica\Steam Boat Willi.mp3", 0.03)
    while True:
        run_menu(screen)
        puntaje = run_game(screen)
        nickname = run_nickname(screen)
        guardar_juego (nickname, puntaje, r"json\jugadores.json")
    
main()