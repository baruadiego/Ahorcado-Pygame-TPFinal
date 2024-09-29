import re, json, pygame

def buscar_en_lista (lista: list, value) -> bool:
    """
    La funcion busca un elemento recibido por parametro en una lista

    Args:
        lista (list): lista a recorrer
        value (_type_): valor que deseamos buscar

    Returns:
        bool: Retorna True si el valor esta en la lista, en caso contrario retrna False.
    """
    esta = False

    for elemento in lista:
        if elemento == value:
            esta = True
            break
    
    return esta

def bubble_sort(lista: list, key=lambda x: x, descendente: bool = False) -> None:
    """Ordena una lista en su lugar utilizando el algoritmo de ordenamiento por burbuja.

    Args:
        lista (list): La lista a ordenar.
        key (_type_, optional): Una función que extrae un valor de comparación de cada elemento de la lista.
                                No devuelve nada, pero modifica la lista.
        descendente (bool, optional): Si es True, ordena la lista en orden descendente. Por defecto es False (orden ascendente).
    """
    for i in range(len(lista) - 1):
        for j in range(i + 1, len(lista)):
            # Comparar usando la clave proporcionada
            if (key(lista[i]) > key(lista[j]) and not descendente) or (key(lista[i]) < key(lista[j]) and descendente):
                # Intercambiar los elementos
                lista[i], lista[j] = lista[j], lista[i]

def crear_matriz (filas: int, columnas: int) -> list:
    """
    Crea una matriz (lista de listas) con las dimensiones especificadas, inicializada con el valor "-".

    Args:
        filas (int): El número de filas de la matriz.
        columnas (int): El número de columnas de la matriz.

    Returns:
        list: Una matriz de tamaño "filas" x "columnas", inicializada con el valor "-".
    """
    matriz = [["-"] * columnas for _ in range (filas)]
    return matriz

def play_sound (path: str, volume: int) -> None:
    """
    Reproduce un sonido con el volumen especificado.

    Args:
        path (str): La ruta del archivo de sonido.
        volume (int): El volumen del sonido, entre 0 (silencio) y 1 (máximo).
    """
    sound = pygame.mixer.Sound(path)
    sound.set_volume(volume)
    sound.play()

def fuente(tamaño_fuente: int) -> pygame.font.Font:
    """
    Crea y devuelve una fuente de Pygame con el tamaño especificado.

    Args:
        tamaño_fuente (int): El tamaño de la fuente a crear.

    Returns:
        pygame.font.Font: Una instancia de la fuente con el tamaño especificado.
    """
    font = pygame.font.SysFont(None, tamaño_fuente)
    
    return font

def guardar_juego (nickname: str, puntaje : int, path: str) -> None:
    """
    Guarda la información del juego en un archivo JSON.

    Args:
        nickname (str): El nombre del jugador.
        puntaje (int): El puntaje del jugador.
        path (str): La ruta del archivo JSON donde se guardará la información.
    """
    jugador = {}
    jugador ["nombre"] = nickname
    jugador ["puntaje"] = puntaje

    lista_jugadores = parser_json (path, "jugadores")
    lista_jugadores.append (jugador)
    actualizar_json (path, "jugadores", lista_jugadores)

def parser_csv (path: str) -> list:
    """
    Lee un archivo CSV y devuelve una lista de los valores de la primera columna.

    Args:
        path (str): La ruta del archivo CSV.

    Returns:
        list: Una lista de los valores de la primera columna del archivo CSV.
    """
    lista = []

    try:
        with open (path, "r", encoding="utf8") as archivo:
            for linea in archivo:
                auxiliar = re.split (",|\n", linea)
                lista.append (auxiliar[0])
    except FileNotFoundError:
        print (f"La ruta '{path}' ha sido modificada")

    return lista

def parser_json (path: str, clave: str) -> list | dict:
    """
    La función lee un archivo Json y carga sus datos en una lista.

    Args:
        path (str): dirección del archivo Json a leer
        clave (str): Clave por el cual se va a leer el archivo Json

    Returns:
        list | dict: se retornan los datos del archivo Json
    """
    retorno = []

    try:
        with open (path, "r", encoding= "utf8") as archivo:
            diccionario = json.load(archivo)
        
        retorno = diccionario[clave]
        
    except FileNotFoundError:
        print ("El archivo no existe o la ruta es incorrecta")

    return retorno

def actualizar_json (path: str, clave: str, elemento):
    """
    La función escribe en un archivo Json los datos recibidos.

    Args:
        path (str): dirección del archivo Json a escribir
        elemento: datos a escribir en el JSon
        clave (str): Clave por el cuál se va a guardar el archivo Json

    """
    diccionario = {}
    diccionario [clave] = elemento

    with open (path, "w", encoding = "utf8") as archivo:
        json.dump (diccionario, archivo, indent=4)

def zfill_propio (cadena: str, largo: int) -> str:
    """Hace que el string pase a tener la cantidad de caracteres que recibe y los completa con 0 por delante de la cadena. Si son menos a la cantidad de caracteres existentes, queda la cantidad de caracteres existentes

    Args:
        cadena (str): cadena a verificar
        largo (int): el largo final de la cadena

    Returns:
        La cadena con el largo pasado por parámetro
    """
    cadena_zfill = cadena
    if (type (cadena) == str) and (len(cadena) > 0):
        if len (cadena) < largo:
            cadena_zfill = "0" * (largo - len(cadena))
            cadena_zfill += cadena

    return cadena_zfill