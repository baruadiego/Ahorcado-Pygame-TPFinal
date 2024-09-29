from classComodin import *
from classBoton import Boton

def instanciar_comodines (x: int, y: int, width: int, height: int) -> tuple[Aumentar_tiempo, Revelar_letra, Multiplicar_tiempo_restante]:
    """
    Crea instancias de comodines para un juego.

    Args:
        x (int): Coordenada x inicial para el primer comodín.
        y (int): Coordenada y para todos los comodines.
        width (int): Ancho de cada comodín.
        height (int): Alto de cada comodín.

    Returns:
        tuple[Aumentar_tiempo, Revelar_letra, Multiplicar_tiempo_restante]: Tupla con las instancias de los comodines creados.
    """
    comodin_tiempo_extra =  Aumentar_tiempo (Boton ((x, y), (width, height), r"image\comodines\30 segundos\Comodín 30 segundos.png", r"image\comodines\30 segundos\Comodín 30 segundos activo.png"), r"image\comodines\30 segundos\Comodín 30 segundos no.png")
    x += width
    comodin_revelar_letra = Revelar_letra (Boton ((x,y), (width, height), r"image\comodines\Adivinar letra\Comodin adivinar letra.png", r"image\comodines\Adivinar letra\Comodin adivinar letra activo.png"), r"image\comodines\Adivinar letra\Comodin adivinar letra no.png")
    x += width
    comodin_multiplicar_puntos = Multiplicar_tiempo_restante (Boton ((x,y), (width, height), r"image\comodines\Multiplicar puntaje\Comodin x2 tiempo.png", r"image\comodines\Multiplicar puntaje\Comodin x2 tiempo activo.png"), r"image\comodines\Multiplicar puntaje\Comodin x2 tiempo no.png")

    return comodin_tiempo_extra, comodin_revelar_letra, comodin_multiplicar_puntos