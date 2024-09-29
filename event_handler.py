from classText_box import Text_box
from funciones_event_handler import *
import pygame

def event_mousemotion_menu (event, boton_menu: Boton, boton_menu_score: Boton) -> None:
    """
    Maneja el evento de movimiento del mouse en el menú principal del juego.

    Args:
        event (pygame.event.Event): Objeto de evento de Pygame.
        boton_menu (Boton): Objeto Boton para el botón de jugar en el menú.
        boton_menu_score (Boton): Objeto Boton para el botón de puntajes en el menú.
    """
    if (boton_menu.get_rect().collidepoint(event.pos)):
        colisionar_boton (boton_menu, boton_menu_score)
    elif (boton_menu_score.get_rect().collidepoint(event.pos)):
        colisionar_boton (boton_menu_score, boton_menu)
    else:
        boton_menu.quitar_colision()
        boton_menu_score.quitar_colision()
        pygame.mouse.set_system_cursor(pygame.SYSTEM_CURSOR_ARROW)

def event_mousebuttondown_menu (event, run: bool, scores: bool, boton_menu: Boton, boton_menu_score: Boton) -> bool:
    """
    Maneja el evento de clic de mouse en el menú principal del juego.

    Args:
        event (pygame.event.Event): Objeto de evento de Pygame.
        run (bool): Estado de ejecución del juego.
        scores (bool): Estado de la pantalla de puntajes.
        boton_menu (Boton): Objeto Boton para el botón de jugar en el menú.
        boton_menu_score (Boton): Objeto Boton para el botón de puntajes en el menú.

    Returns:
        tuple: Nuevo estado de ejecución del juego y estado de la pantalla de puntajes.
    """
    if (boton_menu.get_rect().collidepoint(event.pos)):
        play_sound (r"musica\sonidos\Jugar.mp3", 0.03)
        run = False

    elif (boton_menu_score.get_rect().collidepoint(event.pos)):
        scores = True
    
    return run, scores

def event_mousemotion_scores (event, boton_return: Boton) -> None:
    """
    Maneja el evento de movimiento del mouse en la pantalla de puntajes.

    Args:
        event (pygame.event.Event): Objeto de evento de Pygame.
        boton_return (Boton): Objeto Boton para el botón de retorno a menú en la pantalla de puntajes.
    """
    if (boton_return.get_rect().collidepoint(event.pos)):
        boton_return.colisionar()
    else:
        boton_return.quitar_colision()
        pygame.mouse.set_system_cursor (pygame.SYSTEM_CURSOR_ARROW)

def event_mousebuttondown_scores (event, run, boton_return: Boton) -> bool:
    """
    Maneja el evento de clic de mouse en la pantalla de puntajes.

    Args:
        event (pygame.event.Event): Objeto de evento de Pygame.
        run (bool): Estado de ejecución del juego.
        boton_return (Boton): Objeto Boton para el botón de retorno a menú en la pantalla de puntajes.

    Returns:
        bool: Nuevo estado de ejecución del juego.
    """
    if (boton_return.get_rect().collidepoint(event.pos)): #inicia juego
        run = False
        boton_return.quitar_colision()
    
    return run

def event_mousemotion_game (event, caja_texto: Text_box, comodin_tiempo_extra: Comodin, comodin_revelar_letra: Comodin, comodin_multiplicar_puntos: Comodin, matriz_letras: list):
    """
    Maneja el evento de movimiento del mouse en la pantalla de juego. En caso de aber colisiones realta
    los iconos colisionados con el cursor.

    Args:
        event (pygame.event.Event): Objeto de evento de Pygame.
        caja_texto (Text_box): Objeto Text_box para la caja de texto donde se ingresa la letra.
        comodin_tiempo_extra (Comodin): Objeto Comodin para el comodín de tiempo extra.
        comodin_revelar_letra (Comodin): Objeto Comodin para el comodín de revelar letra.
        comodin_multiplicar_puntos (Comodin): Objeto Comodin para el comodín de multiplicar puntos.
        matriz_letras (list): Lista de objetos Boton representando el teclado de letras.
    """
    if (comodin_tiempo_extra.get_boton().get_rect().collidepoint(event.pos)):
        colisionar_comodin (comodin_tiempo_extra, comodin_multiplicar_puntos, comodin_revelar_letra)
        
    elif (comodin_multiplicar_puntos.get_boton().get_rect().collidepoint(event.pos)):
        colisionar_comodin (comodin_multiplicar_puntos, comodin_tiempo_extra, comodin_revelar_letra)

    elif (comodin_revelar_letra.get_boton().get_rect().collidepoint(event.pos)):
        colisionar_comodin (comodin_revelar_letra, comodin_multiplicar_puntos, comodin_tiempo_extra)

    elif caja_texto.get_rect().collidepoint(event.pos):
        pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_IBEAM)
    
    else:
        descolisionar_comodines (comodin_multiplicar_puntos, comodin_revelar_letra, comodin_tiempo_extra)
        tecla_colisionada = colisionar_teclas (event, matriz_letras)
        
        if not tecla_colisionada:
            pygame.mouse.set_system_cursor (pygame.SYSTEM_CURSOR_ARROW)

def event_mousebuttondown_game (event, nivel: Game, comodin_tiempo_extra: Comodin, comodin_revelar_letra: Comodin, comodin_multiplicar_puntos: Comodin, matriz_letras: list):
    """
    Maneja el evento de clic de mouse en la pantalla de juego.

    Args:
        event (pygame.event.Event): Objeto de evento de Pygame.
        nivel (Game): Objeto Game que representa el estado del juego.
        comodin_tiempo_extra (Comodin): Objeto Comodin para el comodín de tiempo extra.
        comodin_revelar_letra (Comodin): Objeto Comodin para el comodín de revelar letra.
        comodin_multiplicar_puntos (Comodin): Objeto Comodin para el comodín de multiplicar puntos.
        matriz_letras (list): Lista de objetos Boton representando el teclado de letras.
    """
    if comodin_tiempo_extra.get_boton().get_rect().collidepoint(event.pos):
        accionar_comodin (comodin_tiempo_extra, nivel)
        play_sound(r"musica\sonidos\Comodin.mp3", 0.1)

    elif comodin_revelar_letra.get_boton().get_rect().collidepoint(event.pos):
        accionar_comodin (comodin_revelar_letra, nivel)
        play_sound(r"musica\sonidos\Comodin.mp3", 0.1)

    elif comodin_multiplicar_puntos.get_boton().get_rect().collidepoint(event.pos):
        accionar_comodin (comodin_multiplicar_puntos, nivel)
        play_sound(r"musica\sonidos\Comodin.mp3", 0.1)

    for i in range (len(matriz_letras)):
        for j in range (len(matriz_letras[0])):
            if (matriz_letras[i][j].get_boton().get_rect().collidepoint(event.pos) and (matriz_letras[i][j].get_utilizado()==False)):
                matriz_letras[i][j].utilizar(nivel)

def event_keydown_game (event, nivel: Game, caja_texto: Text_box, matriz_letras: list):
    """
    Maneja el evento de tecla presionada en la pantalla de juego.

    Args:
        event (pygame.event.Event): Objeto de evento de Pygame.
        nivel (Game): Objeto Game que representa el estado del juego.
        caja_texto (Text_box): Objeto Text_box para la caja de texto donde se ingresa la letra.
        matriz_letras (list): Lista de objetos Boton representando el teclado de letras.
    """
    if caja_texto.estado:
                
        if event.key == pygame.K_RETURN:
            if caja_texto.get_text() != "":
                acierto = nivel.realizar_intento (caja_texto.get_text())
                cambiar_tecla (matriz_letras, caja_texto.get_text(), acierto)
                caja_texto.set_text ("")

        elif event.key == pygame.K_BACKSPACE:
            caja_texto.set_text (caja_texto.get_text()[:-1])

        else:
            if len (caja_texto.get_text()) == 0:
                auxiliar = event.unicode
                if auxiliar.isalpha():
                    caja_texto.set_text (auxiliar.upper())
                    play_sound("musica\sonidos\Keydown.mp3", 0.1)

def event_time_game (bandera_10_segundos: bool, comodin_multiplicar_puntos: Comodin) -> bool:
    """
    Maneja el evento de tiempo en la pantalla de juego.

    Args:
        bandera_10_segundos (bool): Indica si ya se activó la bandera de 10 segundos.
        comodin_multiplicar_puntos (Comodin): Objeto Comodin para el comodín de multiplicar puntos.

    Returns:
        bool: Nuevo estado de la bandera de 10 segundos.
    """
    if bandera_10_segundos == False and comodin_multiplicar_puntos.get_utilizado() == False:
        comodin_multiplicar_puntos.cambiar_estado ()
        bandera_10_segundos = True

    return bandera_10_segundos

def event_keydown_nickname (event, nickname_caja_texto: Text_box, run: bool) -> bool:
    """
    Maneja el evento de tecla presionada en la pantalla de ingreso de nickname.

    Args:
        event (pygame.event.Event): Objeto de evento de Pygame.
        nickname_caja_texto (Text_box): Objeto Text_box para la caja de texto donde se ingresa el nickname.
        run (bool): Estado de ejecución del juego.

    Returns:
        bool: Nuevo estado de ejecución del juego.
    """
    if nickname_caja_texto.estado:
        if event.key == pygame.K_RETURN:
            if nickname_caja_texto.get_text() != "":
                run = False
                play_sound (r"musica\sonidos\Ok.mp3", 0.03)

        elif event.key == pygame.K_BACKSPACE:
            nickname_caja_texto.set_text (nickname_caja_texto.get_text()[:-1])
            play_sound (r"musica\sonidos\Keydown.mp3", 0.1)

        else:
            if len (nickname_caja_texto.get_text()) < 5 and event.unicode.isalnum():
                nickname_caja_texto.set_text (nickname_caja_texto.get_text() + event.unicode.upper())
                play_sound (r"musica\sonidos\Keydown.mp3", 0.1)

    return run