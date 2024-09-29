import pygame
class Text_box:
    def __init__(self, x: int, y: int, width: int, height: int, color_activo: tuple, color_inactivo: tuple) -> None:
        """
        Inicializador de la clase para una caja de texto.

        Args:
            x (int): Coordenada x de la caja de texto.
            y (int): Coordenada y de la caja de texto.
            width (int): Ancho de la caja de texto.
            height (int): Alto de la caja de texto.
            color_activo (tuple): Color de la caja cuando está activa (en formato RGB tuple).
            color_inactivo (tuple): Color de la caja cuando está inactiva (en formato RGB tuple).
        """
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.rect = pygame.Rect(x, y, self.width, self.height)
        self.color_inactivo = color_inactivo
        self.color_activo = color_activo
        self.color = color_inactivo
        self.estado = False
        self.text = ""
    
    # Getters
    def get_x(self) -> int:
        return self.x
    
    def get_y(self) -> int:
        return self.y

    def get_width(self) -> int:
        return self.width

    def get_height(self) -> int:
        return self.height

    def get_rect(self) -> pygame.Rect:
        return self.rect

    def get_color_inactivo(self) -> tuple:
        return self.color_inactivo

    def get_color_activo(self) -> tuple:
        return self.color_activo

    def get_color(self) -> tuple:
        return self.color

    def get_estado(self) -> bool:
        return self.estado
    
    def get_text (self) -> str:
        """Retorna el texto actual dentro de la caja de texto.

        Returns:
            str: Texto actual dentro de la caja de texto.
        """
        return self.text

    # Setters
    def set_x(self, x) -> int:
        self.x = x
    
    def set_y(self, y) -> int:
        self.y = y
    
    def set_width(self, width: int) -> None:
        """Establece el ancho de la caja de texto y actualiza el ancho del rectángulo correspondiente.

        Args:
            width (int): Nuevo ancho de la caja de texto.
        """
        self.width = width
        self.rect.width = width  # Actualiza el ancho del rectángulo también

    def set_height(self, height: int) -> None:
        self.height = height

    def set_rect(self, rect: pygame.Rect) -> None:
        self.rect = rect

    def set_color_inactivo(self, color_inactivo: tuple) -> None:
        self.color_inactivo = color_inactivo

    def set_color_activo(self, color_activo: tuple) -> None:
        self.color_activo = color_activo

    def set_color(self, color: tuple) -> None:
        self.color = color

    def set_estado(self, estado: bool) -> None:
        """Establece el estado activo/inactivo de la caja de texto y ajusta el color correspondiente.

        Args:
            estado (bool): Nuevo estado de la caja de texto (True para activo, False para inactivo).
        """
        self.estado = estado

        if self.estado == True:
            self.color = self.color_activo
        else:
            self.color = self.color_inactivo

    def set_text (self, text: str) -> None:
        """Establece el texto dentro de la caja de texto.

        Args:
            text (str): Texto a establecer dentro de la caja de texto.
        """
        self.text = text

    def cambiar_estado (self) -> None:
        """Cambia el estado activo/inactivo de la caja de texto y ajusta el color correspondiente."""
        self.estado = not self.estado

        if self.estado == True:
            self.color = self.color_activo
        else:
            self.color = self.color_inactivo
