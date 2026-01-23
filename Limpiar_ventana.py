"""
    Primer prueba limpiar una pantalla
"""
#region imports
import pygame as pg
from OpenGL.GL import *
#endregion

#region constante
# defino una constante para el tamaño de la pantalla
SCREEN_SIZE = (800,600)
#colores de la ventana
SCREEN_COLOR = (0.5,0.0,0.25,1.0)
# colores red,green, blue, opacity
# indicadores del tipo de ventana que estamos creando, la definicion de OPENGL apunta a un int interno, sistema de doble buffer
WINDOW_CREATION_FLAGS = pg.OPENGL | pg.DOUBLEBUF # doble buffer para la ventana
FRAMERATE = 60
#endregion

#region setup
# lo mas recomendable para que sea constante el framerate
pg.init()
# creo la ventana
screen = pg.display.set_mode(SCREEN_SIZE, WINDOW_CREATION_FLAGS)
clock = pg.time.Clock()
# en python recordar que se puede descomprimir los elementos dentro de una lista o tupla con el operador *lista | *tupla 
glClearColor(*SCREEN_COLOR)
#endregion

#region main loop
running = True
while running:
    #lista de eventos ocurridos desde la ultima llamada
    for event in pg.event.get():
        if (event.type == pg.QUIT or (event.type == pg.KEYDOWN and event.type == pg.K_ESCAPE)):
            running = False
        
    glClear(GL_COLOR_BUFFER_BIT)
    #invierto los fotogramas para mostrar los colores
    pg.display.flip()
    #actualizo el reloj interno
    clock.tick(FRAMERATE)
    
#endregion

#region cleanup
pg.quit()
#endregion