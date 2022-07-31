import pygame
from pygame.locals import *
from OpenGL.GLU import *
from OpenGL.GL import *
from math import pi, cos, sin


vertices = [
    [(-2.5, 0), (2.5, 0), (2.5, 0.5), (-2.5, 0.5)]
]

vertices1 = [
    [(-2.2, 1.2), (2.2, 1.2), (2.2, 1.7), (-2.2, 1.7)]
    ]

vertices2 = [
    [(-2.5, 0), (-2, 0), (-2, 1.2), (-2.5, 1.2)]
    ]

vertices3 = [
    [(2.5, 0), (2, 0), (2, 1.2), (2.5, 1.2)]
    ]

vertices4 = [
    [(2.25, 0.6), (2.75, 0.6), (2.75, 1), (2.25, 1)]
    ]

vertices5 = [
    [(-1.2, 1.2), (-0.2, 1.2), (-0.2, 2), (-1.2, 2)]
    ]

vertices6 = [
    [(1.2, 1.2), (0.2, 1.2), (0.2, 2), (1.2, 2)]
    ]
    
vertices7 = [
    [(-2.5, 0.5), (2.5, 0.5), (2.5, 1.2), (-2.5, 1.2)]
    ]


def desenhar_circulo_vermelho( add_x=0.0, add_y=0.0, raio=0.5):
    glColor3f(1.0, 0.0, 0.0)
    glBegin(GL_POLYGON)
    for i in range(180):
        x_val = raio * cos(i * 2*pi / 180)
        y_val = raio * sin(i * 2*pi / 180)
        glVertex2f(x_val + add_x, y_val + add_y)
    glEnd()
    glFlush()

def desenhar_circulo_amarelo( add_x=0.0, add_y=0.0, raio=0.5):
    glColor3f(1.0, 1.0, 0.0)
    glBegin(GL_POLYGON)
    for i in range(180):
        x_val = raio * cos(i * 2*pi / 180)
        y_val = raio * sin(i * 2*pi / 180)
        glVertex2f(x_val + add_x, y_val + add_y)
    glEnd()
    glFlush()

def desenhar_circulo_cinza( add_x=0.0, add_y=0.0, raio=0.5):
    glColor3f(28.0, 28.0, 28.0)
    glBegin(GL_POLYGON)
    for i in range(180):
        x_val = raio * cos(i * 2*pi / 180)
        y_val = raio * sin(i * 2*pi / 180)
        glVertex2f(x_val + add_x, y_val + add_y)
    glEnd()
    glFlush()

def desenhar_circulo_preto( add_x=0.0, add_y=0.0, raio=0.5):
    glColor3f(0.0, 0.0, 0.0)
    glBegin(GL_POLYGON)
    for i in range(180):
        x_val = raio * cos(i * 2*pi / 180)
        y_val = raio * sin(i * 2*pi / 180)
        glVertex2f(x_val + add_x, y_val + add_y)
    glEnd()
    glFlush()

def desenhar_circulo_azul( add_x=0.0, add_y=0.0, raio=0.5):
    glColor3f(0.0,191.0,255.0)
    glBegin(GL_POLYGON)
    for i in range(180):
        x_val = raio * cos(i * 2*pi / 180)
        y_val = raio * sin(i * 2*pi / 180)
        glVertex2f(x_val + add_x, y_val + add_y)
    glEnd()
    glFlush()
    
def desenhar_elipse(cx, cy, rx, ry):
    theta = 2 * pi / 180
    c = cos(theta)
    s = sin(theta)
    x = 1
    y = 0

    glColor3f(1.0, 0.0, 0.0)
    glBegin(GL_POLYGON)
    for i in range(180):
        glVertex2f(x * rx + cx, y * ry + cy)
        t = x
        x = c * x - s * y
        y = s * t + c * y
    glEnd()
    glFlush()
    
def desenhar_paralama(lista_vertices):
    glColor3f(0.0, 0.0, 0.0)
    glBegin(GL_POLYGON)
    for vertice in lista_vertices:
        glVertex2d(*vertice)
    glEnd()
    glFlush()

def desenhar_perto_janela(lista_vertices):
    glColor3f(1.0, 0.0, 0.0)
    glBegin(GL_POLYGON)
    for vertice in lista_vertices:
        glVertex2d(*vertice)
    glEnd()
    glFlush()

def desenhar_apoio_farol_frontal(lista_vertices):
    glColor3f(1.0, 0.0, 0.0)
    glBegin(GL_POLYGON)
    for vertice in lista_vertices:
        glVertex2d(*vertice)
    glEnd()
    glFlush()
def desenhar_apoio_farol_traseiro(lista_vertices):
    glColor3f(1.0, 0.0, 0.0)
    glBegin(GL_POLYGON)
    for vertice in lista_vertices:
        glVertex2d(*vertice)
    glEnd()
    glFlush()

def desenhar_parachoque_traseiro(lista_vertices):
    glColor3f(0.0, 0.0, 0.0)
    glBegin(GL_POLYGON)
    for vertice in lista_vertices:
        glVertex2d(*vertice)
    glEnd()
    glFlush()

def desenhar_janela_esquerda(lista_vertices):
    glColor3f(0.0, 191.0, 255.0)
    glBegin(GL_POLYGON)
    for vertice in lista_vertices:
        glVertex2d(*vertice)
    glEnd()
    glFlush()

def desenhar_janela_direita(lista_vertices):
    glColor3f(0.0, 191.0, 255.0)
    glBegin(GL_POLYGON)
    for vertice in lista_vertices:
        glVertex2d(*vertice)
    glEnd()
    glFlush()

def desenhar_corpo(lista_vertices):
    glColor3f(1.0, 0.0, 0.0)
    glBegin(GL_POLYGON)
    for vertice in lista_vertices:
        glVertex2d(*vertice)
    glEnd()
    glFlush()

def main():
    pygame.init()
    display = (500, 500)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)

    gluPerspective(70, display[0]/display[1], 1, 10)
    glTranslate(0.0, 0.0, -10)
    glRotatef(0, 0, 0, 0)
    

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                    
                    #TRANSLAÇÃO
                    if event.key == pygame.K_LEFT:
                        glTranslatef(-0.5, 0, 0)
                    if event.key == pygame.K_RIGHT:
                        glTranslatef(0.5, 0, 0)
                    if event.key == pygame.K_UP:
                        glTranslatef(0, 1, 0)
                    if event.key == pygame.K_DOWN:
                        glTranslatef(0, -1, 0)
                        
                    #REFLEXÃO EM CADA EIXO
                    if event.key == pygame.K_a:
                            glScalef(-1,1,1)
                    if event.key == pygame.K_d:
                            glScalef(1,-1,1)
                            
                    #REFLEXÃO NOS DOIS EIXOS
                    if event.key == pygame.K_s:
                        glScalef(-1,-1,1)

            #ESCALA
            if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 4:
                        glTranslatef(0, 0, 1.0)

                    if event.button == 5:
                        glTranslatef(0, 0, -1.0)
        
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        
        desenhar_elipse(0, 1.6, 2, 1.2) # parte de cima do carro
        desenhar_circulo_amarelo(add_x=-2.5, add_y=0.8, raio=0.3) # farol
        for l_vertices in vertices1:
            desenhar_perto_janela(l_vertices)
        for l_vertices in vertices2:
            desenhar_apoio_farol_frontal(l_vertices)
        for l_vertices in vertices3:
            desenhar_apoio_farol_traseiro(l_vertices)
        for l_vertices in vertices4:
            desenhar_parachoque_traseiro(l_vertices)
        for l_vertices in vertices5:
            desenhar_janela_esquerda(l_vertices)
        for l_vertices in vertices6:
            desenhar_janela_direita(l_vertices)
        for l_vertices in vertices7:
            desenhar_corpo(l_vertices)
        for l_vertices in vertices:
            desenhar_paralama(l_vertices)
        desenhar_circulo_preto(add_x=-1.5, add_y=0.2) # roda esquerda
        desenhar_circulo_cinza(add_x=-1.5, add_y=0.2, raio=0.3) # aro roda esquerda
        desenhar_circulo_preto(add_x=1.5, add_y=0.2) # roda direita
        desenhar_circulo_cinza(add_x=1.5, add_y=0.2, raio=0.3) # aro roda esquerda
        desenhar_circulo_azul(add_x=-1.2, add_y=1.6, raio=0.4) # janela esquerda
        desenhar_circulo_azul(add_x=1.2, add_y=1.6, raio=0.4) # janela direita
        desenhar_circulo_vermelho(add_x=-2.25, add_y=1.4, raio=0.3) # complemento capô superior esquerdo
        desenhar_circulo_vermelho(add_x=2.25, add_y=1.4, raio=0.3) # complemento capô superior esquerdo
        desenhar_circulo_preto(add_x=-2.5, add_y=0.2, raio=0.3) # complemento para-choque esquerdo
        desenhar_circulo_preto(add_x=2.5, add_y=0.2, raio=0.3) # complemento para-choque direito
        
        pygame.display.flip()
        
if __name__ == "__main__":
    main()
