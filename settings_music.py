import pygame

def play_music(path: str, volume: float) -> None:
    """
    inicializa la cancion principla del juego y la reroduce en loop

    Args:
        path (str): ruta donde se encuentra el tema a reproducir
        volume (float): volumen de la cancion
    """
    pygame.mixer.init()
    pygame.mixer.music.load(path)
    pygame.mixer.music.set_volume (volume)
    pygame.mixer.music.play(-1)