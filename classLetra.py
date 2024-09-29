from classBoton import Boton
from classGamesSet import Game
class Letra:
    def __init__(self, caracter: str, boton: Boton, path_correcto: str, path_incorrecto: str) -> None:
        """Inicializa una letra con su caracter asociado, botón de representación visual y rutas de imágenes.

        Args:
            caracter (str): Caracter representado por la letra.
            boton (Boton): Objeto botón que representa visualmente la letra.
            path_correcto (str): Ruta de la imagen cuando la letra es seleccionada correctamente.
            path_incorrecto (str): Ruta de la imagen cuando la letra no es seleccionada correctamente.
        """
        self.__caracter = caracter.upper()
        self.__boton = boton
        self.__path_correcto = path_correcto
        self.__path_incorrecto = path_incorrecto
        self.__utilizado = False

    # Getters
    def get_caracter(self) -> str:
        return self.__caracter

    def get_boton(self) -> Boton:
        return self.__boton

    def get_path_correcto(self) -> str:
        return self.__path_correcto

    def get_path_incorrecto(self) -> str:
        return self.__path_incorrecto

    def get_utilizado(self) -> bool:
        return self.__utilizado

    # Setters
    def set_caracter(self, caracter: str) -> None:
        self.__caracter = caracter

    def set_boton(self, boton: Boton) -> None:
        self.__boton = boton

    def set_path_correcto(self, path_correcto: str) -> None:
        self.__path_correcto = path_correcto

    def set_path_incorrecto(self, path_incorrecto: str) -> None:
        self.__path_incorrecto = path_incorrecto

    def set_utilizado(self, utilizado: bool) -> None:
        self.__utilizado = utilizado

    #metodos
    def cambiar_estado (self) -> None: #revisar
        self.__utilizado = not self.__utilizado
        
        if self.__utilizado == False:
            self.__boton.set_imagen (self.__boton.get_imagen_no_colision())

    def utilizar (self, nivel: Game) -> None:
        acierto = nivel.realizar_intento (self.get_caracter())
        self.__utilizado = True

        if acierto == False:
            self.__boton.set_imagen (self.__path_incorrecto)
        else:
            self.__boton.set_imagen (self.__path_correcto)
