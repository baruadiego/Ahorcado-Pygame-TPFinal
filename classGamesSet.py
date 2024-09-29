import time, random
from funciones_generales import *

class Game:
    def __init__(self, tiempo: int, reintentos: int, puntaje: int) -> None:
        """
        Instancia un juego con los parámetros dados.

        Args:
            tiempo (int): Límite de tiempo inicial para el juego.
            reintentos (int): Número de intentos permitidos para el juego.
            puntaje (int): Puntaje inicial del jugador.
        """
        self.__categoria = None
        self.__palabra = None
        self.__palabras_utilizadas = []
        self.__tiempo = tiempo
        self.__puntaje = puntaje
        self.__multiplicar = False
        self.__reintentos = reintentos
        self.__errores = 0
        self.__lista_aciertos = []
        self.__lista_intentos = []
        self.__tiempo_inicio = None
        self.__tiempo_final = None
        self.__victoria = False
        self.__derrota = False
        self.__nivel_terminado = False

    #getters
    def get_categoria(self) -> str:
        return self.__categoria
    
    def get_palabras_utilizadas(self) -> list:
        return self.__palabras_utilizadas
    
    def get_palabra(self) -> str:
        return self.__palabra

    def get_tiempo(self) -> int:
        return self.__tiempo

    def get_puntaje(self) -> int:
        return self.__puntaje
    
    def get_multiplicar(self) -> bool:
        return self.__multiplicar

    def get_reintentos(self) -> int:
        return self.__reintentos
    
    def get_errores (self) -> int:
        return self.__errores
    
    def get_lista_aciertos (self) -> list:
        return self.__lista_aciertos
    
    def get_tiempo_inicio (self) -> float:
        return self.__tiempo_inicio
    
    def get_tiempo_final (self) -> float:
        return self.__tiempo_final

    def get_victoria(self) -> bool:
        return self.__victoria

    def get_derrota(self) -> bool:
        return self.__derrota
    
    def get_nivel_terminado(self) -> bool:
        return self.__nivel_terminado

    def get_tiempo_transcurrido (self) -> float:
        return time.time() - self.__tiempo_inicio
    
    def get_tiempo_restante (self) -> float:
        return self.__tiempo - self.get_tiempo_transcurrido()
    
    def get_lista_intentos(self) -> list:
        return self.__lista_intentos

    #setters
    def set_categoria(self, categoria: str) -> None:
        self.__categoria = categoria

    def set_palabras_utilizadas(self, palabras_utilizadas: list) -> None:
        self.__palabras_utilizadas =  palabras_utilizadas

    def set_lista_intentos(self, lista: list) -> None:
        self.__lista_intentos = lista

    def set_palabra(self, palabra: str) -> None:
        self.__palabra = palabra

    def set_tiempo(self, tiempo: int) -> None:
        self.__tiempo = tiempo

    def set_puntaje(self, puntaje: int) -> None:
        self.__puntaje = puntaje

    def set_multiplicar(self, estado) -> None:
        self.__multiplicar = estado

    def set_reintentos(self, reintentos: int) -> None:
        self.__reintentos = reintentos

    def set_errores (self, errores) -> int:
        self.__errores = errores

    def set_victoria(self, victoria: bool) -> None:
        self.__victoria = victoria

    def set_derrota(self, derrota: bool) -> None:
        self.__derrota = derrota

    def set_nivel_terminado (self, nivel_terminado: bool) -> None:
        self.__nivel_terminado = nivel_terminado

    #metodos
    def __seleccionar_tematica (self, opcion: int) -> list:
        """
        Selecciona un tema (categoría de palabras) según la opción recibida.

        Args:
            opcion (int): La opción seleccionada que representa una categoría.

        Returns:
            list: Una lista de palabras (cadenas) correspondientes a la categoría seleccionada.
        """

        match opcion:
            case 1:
                path = r"palabras\DEPORTES.csv"
            case 2:
                path = r"palabras\ENTRETENIMIENTO.csv"
            case 3:
                path = r"palabras\HISTORIA.csv"
            case 4:
                path = r"palabras\MATEMATICA.csv"
            case 5:
                path = r"palabras\MUSICA.csv"
            case 6:
                path = r"palabras\PROGRAMACION.csv"

        lista_palabras = parser_csv (path)
        return lista_palabras

    def __seleccionar_palabra (self, cantidad_categorias: int) -> None:
        """
        Selecciona al azar una palabra de una categoría elegida al azar.

        Args:
            cantidad_categorias (int): El número de categorías disponibles.
        """
        palabra_no_utilizada = False

        while palabra_no_utilizada == False:
            opcion = random.randint (1,cantidad_categorias)
            lista_palabras = self.__seleccionar_tematica (opcion)

            palabra_seleccionada = lista_palabras[random.randint (1, len(lista_palabras) - 1)]
            categoria_seleccionada = lista_palabras[0]
            if buscar_en_lista (self.__palabras_utilizadas, palabra_seleccionada) == False:
                palabra_no_utilizada = True

        self.__palabra = palabra_seleccionada.upper()
        self.__lista_aciertos = ["_"] * len(self.__palabra)
        self.__categoria = categoria_seleccionada.upper()
        self.__palabras_utilizadas.append (self.__palabra)

    def iniciar_nivel (self) -> None:
        """
        Inicia un nuevo nivel seleccionando una palabra de una categoría elegida al azar y activa el 
        cronómetro.
        """
        self.__seleccionar_palabra (6)
        self.__tiempo_inicio = time.time()

    def terminar_nivel (self) -> None:
        """
        Finaliza el nivel actual, actualizando el estado del juego según el desempeño del jugador.
        """
        if buscar_en_lista (self.__lista_aciertos, "_") == False:
            self.__victoria = True

            if self.__multiplicar:
                self.__puntaje += int(self.get_tiempo_restante()) * 2
                self.__multiplicar = False
            else:
                self.__puntaje += int(self.get_tiempo_restante())

        else:
            self.__derrota = True

        self.__tiempo_final = time.time()
        self.__nivel_terminado = True

    def nuevo_nivel (self, tiempo: int) -> None:
        """
        Reinicia el estado del juego para comenzar un nuevo nivel con el límite de tiempo dado.

        Args:
            tiempo (int): Límite de tiempo para el nuevo nivel.
        """
        self.__tiempo = tiempo
        self.__victoria = False
        self.__derrota = False
        self.__nivel_terminado = False
        self.__errores = 0
        self.__lista_intentos = []
        self.iniciar_nivel()

    def buscar_letra (self, letra: str) -> bool:
        """
        Busca una letra intentada en la palabra actual, actualiza las adivinanzas correctas y devuelve si la letra es correcta.

        Args:
            letra (str): La letra intentada por el jugador.

        Returns:
            bool: True si la letra se encuentra en la palabra, False en caso contrario.
        """
        acierto = False
        if self.__palabra.count(letra) != 0:
            acierto = True
            apariciones = self.__palabra.count(letra)
            
            for i in range (len(self.__palabra)):
                if letra == self.__palabra[i]:
                    self.__lista_aciertos[i] = letra
                    apariciones -= 1
                    if apariciones == 0:
                        break

        return acierto

    def realizar_intento(self, letra: str) -> bool:
        """
        Verifica si una letra ingresada es correcta, actualiza el estado del juego y devuelve el resultado.

        Args:
            letra (str): La letra ingresada por el jugador.

        Returns:
            bool: True si la letra es correcta, False en caso contrario.
        """
        acierto = None

        if buscar_en_lista (self.__lista_intentos, letra) == False:
            self.__lista_intentos.append(letra)
            acierto = self.buscar_letra(letra)

            if acierto:
                self.__puntaje += 10
            else:
                if self.__puntaje >= 5:
                    self.__puntaje -= 5
                self.__errores += 1

            if buscar_en_lista(self.__lista_aciertos, "_") == False or self.__reintentos == self.__errores:
                self.terminar_nivel()

        return acierto