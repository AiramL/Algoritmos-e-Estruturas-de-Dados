################################################################
#                                                              #
#   Lucas Airam Castro de Souza                                #
#   Gabriel Monteiro de Castro Xará Wanderley                  #
#                                                              #
#   Universidade Federal do Rio de Janeiro                     #
#   Algoritmos e Estruturas de Dados                           #
#                                                              #
################################################################




import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *


class Pyramid():

    vertices = (
        (1,-1,-1),
        (1,1,-1),
        (-1,1,-1),
        (-1,-1,-1),
        (0,0,1)
        )

    edges = (
        (0,1),
        (0,3),
        (0,4),
        (1,4),
        (1,2),
        (2,4),
        (2,3),
        (3,4)
        )
    def __init__(self):
        self.edges = Pyramid.edges
        self.vertices = Pyramid.vertices

        
    def draw(self):
        glLineWidth(5);
        glBegin(GL_LINES);

        for edge in self.edges:
            for vertex in edge:
                glVertex3fv(self.vertices[vertex])
                glColor3f(1,0,0)
        glEnd();

class toro():

    vertices = (
        (1,-1,-1),
        (1,1,-1),
        (-1,1,-1),
        (-1,-1,-1),
        (0,0,1)
        )

    edges = (
        (0,1),
        (0,3),
        (0,4),
        (1,4),
        (1,2),
        (2,4),
        (2,3),
        (3,4)
        )
    def __init__(self):
        self.edges = Pyramid.edges
        self.vertices = Pyramid.vertices

        
    def draw(self):
        glLineWidth(5);
        glBegin(GL_LINES);

        for edge in self.edges:
            for vertex in edge:
                glVertex3fv(self.vertices[vertex])
                glColor3f(1,0,0)
        glEnd();

class barra():

    vertices = (
        (1,-1,-1),
        (1,1,-1),
        (-1,1,-1),
        (-1,-1,-1),
        (0,0,1)
        )

    edges = (
        (0,1),
        (0,3),
        (0,4),
        (1,4),
        (1,2),
        (2,4),
        (2,3),
        (3,4)
        )
    def __init__(self, posicaoX=0, posicaoY=0, posicaoZ=0):
        self.edges = barra.edges
        self.vertices = barra.vertices
        if (posicaoX or posicaoY or posicaoZ):
            self.mudar_posicao(posicaoX,posicaoY,posicaoZ)
            

    def mudar_posicao(self,X,Y,Z):
        nova_posicao = []
        for vertice in self.vertices:
            nova_posicao.append((vertice[0]+X, vertice[1]+Y, vertice[2]+Z))
        self.vertices = (nova_posicao)
            
        
    def draw(self):
        glLineWidth(5);
        glBegin(GL_LINES);

        for edge in self.edges:
            for vertex in edge:
                glVertex3fv(self.vertices[vertex])
                glColor3f(1,0,0)
        glEnd();







def main():
    pygame.init();
    display = (800,800);
    pygame.display.set_mode(display, DOUBLEBUF|OPENGL);

    gluPerspective(45, (display[0]/display[1]), 0.1, 50);

    glTranslatef(0,0,-5);

    p = barra();

    vel = 0.1;

    clock = pygame.time.Clock()
    while True:
        clock.tick(60);
        for event in  pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit();
                quit();

        keys = pygame.key.get_pressed();                # guarda a tecla que o usuario pressiona

        if keys[pygame.K_LEFT]:                         # seta esquerda move a perspectiva para a esquerda
            glTranslatef(-vel,0,0);
        if keys[pygame.K_RIGHT]:                        # seta direita move a perspectiva para a direita
            glTranslatef(vel,0,0);
        if keys[pygame.K_UP]:                           # seta superior move a perspectiva para cima
            glTranslatef(0,vel,0);              
        if keys[pygame.K_DOWN]:                         # seta inferior move a perspectiva para baixo
            glTranslatef(0,-vel,0);
        if keys[pygame.K_z]:                            # z move a perspectiva para Z positivo
            glTranslatef(0,0,vel);
        if keys[pygame.K_x]:                            # x decrementa coordenada z
            glTranslatef(0,0,-vel);
        if keys[pygame.K_i]:                            # i rotacao no plano jk             
            glRotatef(vel*5,1,0,0);
        if keys[pygame.K_j]:                            # j rotacao no plano ik             
            glRotatef(vel*5,0,1,0);
        if keys[pygame.K_k]:                            # k rotacao no plano ij             
            glRotatef(vel*5,0,0,1);
        if keys[pygame.K_l]:                            # l rotacao negativa no plano jk             
            glRotatef(-vel*5,1,0,0);
        if keys[pygame.K_o]:                            # o rotacao negativa no plano ik             
            glRotatef(-vel*5,0,1,0);
        if keys[pygame.K_p]:                            # p rotacao negativa no plano ij             
            glRotatef(-vel*5,0,0,1);


        #glRotatef(2,1,1,3);
        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT);
        p.draw();
        pygame.display.flip();


main()
        
        
