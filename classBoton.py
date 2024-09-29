import pygame
class Boton:
    def __init__(self, origen: tuple, dimesion: tuple, path: str, path_colision: str) -> None:
        """
        Representa un botón interactivo en la interfaz del juego.

        Args:
            origen (tuple): Las coordenadas (x, y) del centro del botón.
            dimension (tuple): Las dimensiones (ancho, alto) del botón.
            path (str): La ruta de la imagen del botón sin colisión.
            path_colision (str): La ruta de la imagen del botón con colisión.
        """
        self.__imagen_no_colision = path
        self.__imagen = path
        self.__imagen_surface = pygame.image.load(path)
        self.__imagen_colision = path_colision
        self.__colision = False
        self.__origen = origen
        self.__dimension = dimesion
        self.__imagen_surface = pygame.transform.scale(self.__imagen_surface, dimesion)
        self.__rect = self.__imagen_surface.get_rect()
        self.__rect.center = origen

    # Getters
    def get_imagen(self) -> str:
        return self.__imagen

    def get_imagen_colision(self) -> str:
        return self.__imagen_colision
    
    def get_imagen_no_colision(self) -> str:
        return self.__imagen_no_colision
    
    def get_imagen_surface(self) -> str:
        return self.__imagen_surface

    def get_colision(self) -> bool:
        return self.__colision

    def get_origen(self) -> tuple:
        return self.__origen

    def get_dimension(self) -> tuple:
        return self.__dimension

    def get_rect(self) -> pygame.Rect:
        return self.__rect

    # Setters
    def set_imagen(self, imagen: str) -> None:
        """
        Cambia la imagen del botón a la especificada por `path`.

        Args:
            path (str): La nueva ruta de la imagen del botón.
        """
        self.__imagen = imagen
        self.__imagen_surface = pygame.image.load(imagen)
        self.__imagen_surface = pygame.transform.scale(self.__imagen_surface, self.__dimension)

    def set_imagen_colision(self, imagen_colision: str) -> None:
        self.__imagen_colision = imagen_colision

    def set_colision(self, colision: bool) -> None:
        self.__colision = colision
        if colision:
            self.__imagen_surface = pygame.image.load(self.__imagen_colision)
        else:
            self.__imagen_surface = pygame.image.load(self.__imagen_no_colision)
        self.__imagen_surface = pygame.transform.scale(self.__imagen_surface, self.__dimension)

    def set_origen(self, origen: tuple) -> None:
        self.__origen = origen
        self.__rect.center = origen

    def set_dimension(self, dimension: tuple) -> None:
        self.__dimension = dimension
        self.__imagen_surface = pygame.transform.scale(self.__imagen_surface, dimension)
        self.__rect = self.__imagen_surface.get_rect()
        self.__rect.center = self.__origen

    def quitar_colision (self) -> None:
        """
        Desactiva la colisión del botón y restaura la imagen a la versión sin colisión.
        """
        self.__colision = False
        self.set_imagen (self.__imagen_no_colision)

    def colisionar (self) -> None:
        """
        Activa la colisión del botón y cambia la imagen a la versión con colisión.
        Además, cambia el cursor del mouse a una mano para indicar interactividad.
        """
        self.__colision = True
        self.set_imagen (self.__imagen_colision)
        pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)