from classBoton import Boton
from classGamesSet import *
class Comodin:
    def __init__(self, boton: Boton, path_utilizado: str) -> None:
        """
        Representa un comodín interactivo en el juego.

        Args:
            boton (Boton): El botón asociado al comodín.
            path_utilizado (str): La ruta de la imagen que muestra el comodín utilizado.
        """
        self.__boton = boton
        self.__path_utilizado = path_utilizado
        self.__utilizado = False

    def get_boton (self) -> Boton:
        return self.__boton
    
    def get_utilizado (self) -> bool:
        return self.__utilizado
    
    def get_path_utilizado(self):
        return self.__path_utilizado

    def set_path_utilizado(self, path):
        self.__path_utilizado = path

    def set_utilizado (self, estado: bool) -> None:
        self.__utilizado = estado

    def set_boton (self, boton: Boton) -> None:
        self.__boton = boton

    def cambiar_estado (self) -> None:
        """
        Alterna el estado de utilización del comodín y cambia la imagen del botón correspondiente.
        """
        self.__utilizado = not self.__utilizado
        
        if self.__utilizado == True:
            self.__boton.set_imagen (self.__path_utilizado)
        else:
            self.__boton.set_imagen (self.__boton.get_imagen_no_colision())

    def ejecutar (self) -> None:
        self.cambiar_estado()

class Aumentar_tiempo (Comodin):
    def __init__(self, boton: Boton, path_utilizado: str) -> None:
        """
        Representa un comodín que aumenta el tiempo disponible en el juego.

        Args:
            boton (Boton): El botón asociado al comodín.
            path_utilizado (str): La ruta de la imagen que muestra el comodín utilizado.
        """
        super().__init__(boton, path_utilizado)
    
    def ejecutar(self, nivel: Game) -> None:
        """
        Ejecuta la acción del comodín, aumentando el tiempo disponible en el nivel del juego.

        Args:
            nivel (Game): El objeto de tipo Game que representa el nivel del juego.
        """
        nivel.set_tiempo (nivel.get_tiempo() + 30)
        super().ejecutar()

class Revelar_letra (Comodin):
    def __init__(self, boton: Boton, path_utilizado: str) -> None:
        """
        Representa un comodín que revela una letra en el juego.

        Args:
            boton (Boton): El botón asociado al comodín.
            path_utilizado (str): La ruta de la imagen que muestra el comodín utilizado.
        """
        super().__init__(boton, path_utilizado)
    
    def __descubrir_letra (self, nivel: Game) -> None:
        """
        Método privado que revela una letra aleatoria en el juego.

        Args:
            nivel (Game): El objeto de tipo Game que representa el nivel del juego.
        """
        while True:
            i = random.randint (0, len(nivel.get_palabra()) -1)
            letra_descubierta = nivel.get_palabra()[i]
            
            if nivel.get_lista_aciertos().count(letra_descubierta) == 0:
                nivel.get_lista_aciertos()[i] = letra_descubierta
                break

    def ejecutar(self, nivel: Game) -> None:
        """
        Ejecuta la acción del comodín, revelando una letra en el juego.

        Args:
            nivel (Game): El objeto de tipo Game que representa el nivel del juego.
        """
        self.__descubrir_letra(nivel)

        # Verificar si aún hay letras sin revelar
        if buscar_en_lista (nivel.get_lista_aciertos(), "_") == False:
            nivel.terminar_nivel()

        super().ejecutar()

class Multiplicar_tiempo_restante (Comodin):
    def __init__(self, boton: Boton, path_utilizado: str) -> None:
        """
        Representa un comodín que multiplica el tiempo restante por dos en el juego.

        Args:
            boton (Boton): El botón asociado al comodín.
            path_utilizado (str): La ruta de la imagen que muestra el comodín utilizado.
        """
        super().__init__(boton, path_utilizado)

    def ejecutar(self, nivel: Game) -> None:
        """
        Ejecuta la acción del comodín, activando la multiplicación del tiempo restante en el nivel del juego.

        Args:
            nivel (Game): El objeto de tipo Game que representa el nivel del juego.
        """
        nivel.set_multiplicar (True)
        super().ejecutar()