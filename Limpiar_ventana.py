#region imports
import pygame as pg
from OpenGL.GL import *
from OpenGL.GL.shaders import compileProgram, compileShader
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

#region shader
def make_shader(vertex_filename: str, fragment_filename: str) -> int:
    vertex_module = make_shader_module(vertex_filename, GL_VERTEX_SHADER)
    fragment_module = make_shader_module(fragment_filename, GL_FRAGMENT_SHADER)
    return compileProgram(vertex_module, fragment_module)
    # debo vincular para generar el binario
    

def make_shader_module(filename: str, module_type: int) -> int:
    # cargamos el archivo de los vertices y fragmentos
    with open(filename, "r") as file:
        source_code = file.readlines()
    return compileShader(source_code, module_type)
        # extraigo el codigo y le indico a la gpu que lo compile, 

class Renderer:
    SCREEN_COLOR = (0.5,0.0,0.25,1.0)
    
    def __init__(self):
        glClearColor(*Renderer.SCREEN_COLOR)
        # accedo a la variable estatica del color que se debe de renderizar
        
        self.VAO = glGenVertexArrays(1)
        glBindVertexArray(self.VAO)

        self.shader = make_shader("vertex.txt", "fragment.txt")
        
    def draw(self) -> None:
        
        glClear(GL_COLOR_BUFFER_BIT)

        glUseProgram(self.shader)
        glDrawArrays(GL_TRIANGLES, 0, 3)
        
    def destroy(self) -> None:
        
        glDeleteProgram(self.shader)  
#end shader
#region setup


# lo mas recomendable para que sea constante el framerate
pg.init()

# para el control de versiones de OpenGL
pg.display.gl_set_attribute(pg.GL_CONTEXT_MAJOR_VERSION, 3)
pg.display.gl_set_attribute(pg.GL_CONTEXT_MINOR_VERSION, 3)
pg.display.gl_set_attribute(pg.GL_CONTEXT_PROFILE_MASK, pg.GL_CONTEXT_PROFILE_CORE)

# creo la ventana
screen = pg.display.set_mode(SCREEN_SIZE, WINDOW_CREATION_FLAGS)
clock = pg.time.Clock()
renderer = Renderer()
# en python recordar que se puede descomprimir los elementos dentro de una lista o tupla con el operador *lista | *tupla 

#endregion

#region main loop
running = True
while running:
    #lista de eventos ocurridos desde la ultima llamada
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_ESCAPE:
                running = False
    renderer.draw()
    #invierto los fotogramas para mostrar los colores
    pg.display.flip()
    #actualizo el reloj interno
    clock.tick(FRAMERATE)
    
#endregion

#region cleanup
renderer.destroy()
pg.quit()
#endregion