from classComodin import Comodin
from classGamesSet import Game
from classLetra import Letra
from classBoton import Boton
from Comodines import *

def colisionar_boton (boton: Boton, boton_a: Boton) -> None:
    if boton_a.get_colision() == True:
        boton_a.quitar_colision()

    boton.colisionar()

def colisionar_comodin (comodin: Comodin, comodin_a: Comodin, comodin_b: Comodin) -> None:
    if comodin.get_utilizado() == False:
        if comodin_a.get_utilizado() == False and comodin_a.get_boton().get_colision() == True:
            comodin_a.get_boton().quitar_colision()

        if comodin_b.get_utilizado() == False and comodin_b.get_boton().get_colision() == True:
            comodin_b.get_boton().quitar_colision()

        comodin.get_boton().colisionar()

def descolisionar_comodines (comodin: Comodin, comodin_a: Comodin, comodin_b: Comodin) -> None:
    if comodin.get_utilizado() == False and comodin.get_boton().get_colision():
        comodin.get_boton().quitar_colision()

    elif comodin_a.get_utilizado() == False and comodin_a.get_boton().get_colision():
        comodin_a.get_boton().quitar_colision()

    elif comodin_b.get_utilizado() == False and comodin_b.get_boton().get_colision():
        comodin_b.get_boton().quitar_colision()

def accionar_comodin (comodin: Comodin, nivel:Game) -> None:
    if comodin.get_utilizado() == False:
        comodin.ejecutar(nivel)

def colisionar_teclas (event, matriz_letras: list[Letra]) -> bool:
    tecla_colisionada = False

    for i in range (len(matriz_letras)):
        for j in range (len(matriz_letras[0])):
            if matriz_letras[i][j].get_boton().get_rect().collidepoint(event.pos):
                if (matriz_letras[i][j].get_utilizado()==False):
                    matriz_letras[i][j].get_boton().colisionar()
                    tecla_colisionada = True
            else:
                if matriz_letras[i][j].get_boton().get_colision() == True and matriz_letras[i][j].get_utilizado()==False:
                    matriz_letras[i][j].get_boton().quitar_colision()

    return tecla_colisionada

def cambiar_tecla (matriz_letras: list, letra: str, acierto: bool) -> None:
    for i in range (len(matriz_letras)):
        for j in range (len(matriz_letras[0])):
            if (matriz_letras[i][j].get_utilizado()==False) and (matriz_letras[i][j].get_caracter() == letra):
                if acierto:
                    matriz_letras[i][j].get_boton().set_imagen (matriz_letras[i][j].get_path_correcto())
                else:
                    matriz_letras[i][j].get_boton().set_imagen (matriz_letras[i][j].get_path_incorrecto())
                matriz_letras[i][j].cambiar_estado()
                break