# -*- coding: cp1252 -*-
################################################################
#                                                              #
#   Lucas Airam Castro de Souza                                #
#   Gabriel Monteiro de Castro Xará Wanderley                  #
#                                                              #
#   Universidade Federal do Rio de Janeiro                     #
#   Algoritmos e Estruturas de Dados                           #
#                                                              #
################################################################



# -*- coding: cp1252 -*-



import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
from time import sleep



class contar():
    def __init__(self,n):
        self.n = n

class toro_quadrado():

    superior_1 = (0.3,0.3,0)
    superior_2 = (0.3,0.6,0)
    superior_3 = (0.6,0.6,0)
    superior_4 = (0.6,0.3,0)
    


    inferior_1 = (0.3,0.3,-0.1)
    inferior_2 = (0.3,0.6,-0.1)
    inferior_3 = (0.6,0.6,-0.1)
    inferior_4 = (0.6,0.3,-0.1)
    

    
    superior_externo_1 = (0.1,0.1,0)
    superior_externo_2 = (0.1,0.8,0)
    superior_externo_3 = (0.8,0.8,0)
    superior_externo_4 = (0.8,0.1,0)

    inferior_externo_1 = (0.1,0.1,-0.1)
    inferior_externo_2 = (0.1,0.8,-0.1)
    inferior_externo_3 = (0.8,0.8,-0.1)
    inferior_externo_4 = (0.8,0.1,-0.1)



    vertices = (
        # vertices internos

        # superior

        superior_1,         # 0
        superior_2,         # 1
        superior_3,         # 2
        superior_4,         # 3
    
        # inferior

        inferior_1,         # 4
        inferior_2,         # 5
        inferior_3,         # 6
        inferior_4,         # 7
        
        # vertices externos


        # superior

        superior_externo_1, # 8
        superior_externo_2, # 9
        superior_externo_3, # 10
        superior_externo_4, # 11
   
        # inferior

        inferior_externo_1, # 12
        inferior_externo_2, # 13
        inferior_externo_3, # 14
        inferior_externo_4, # 15
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


    surfaces = (
            (0,1,5,4),
            (2,3,7,6),
            (0,3,7,4),
            (1,2,6,5),
            (8,9,13,12),
            (11,10,14,15),
            (8,11,15,12),
            (9,10,14,13),
            (15,7,6,14),
            (10,3,2,11),
            (1,9,10,2),
            (5,13,14,6),
            (5,9,10,6),
        )

    surfaces_2 = (
            (8,0,3,11),
            (12,4,7,15),
            (8,9,1,0),
            (12,13,5,4),
        )



    
    def __init__(self,raio=0,color=[0,1,0],escala=1,posicaoX=0,posicaoY=0,posicaoZ=0):
        self.escala = escala
        self.color = color
        self.x = posicaoX
        self.y = posicaoY
        self.z = posicaoZ
        if(raio):
            self.mudar_raio(raio)
        if(posicaoX or posicaoY or posicaoZ):
            self.mudar_posicao(posicaoX,posicaoY,posicaoZ)
        






    def draw(self):
        # surperficie 1
        glBegin(GL_QUADS)        
        for surface in self.surfaces:
            glColor3fv((self.color[0],self.color[1],self.color[2]))
            for vertex in surface:
                glVertex3fv(self.vertices[vertex])
        glEnd();

        # superficie 2

        glBegin(GL_POLYGON)        
        for surface in self.surfaces_2:
            glColor3fv((self.color[0],self.color[1],self.color[2]))
            for vertex in surface:
                glVertex3fv(self.vertices[vertex])
        glEnd();


    def mudar_posicao(self,X,Y,Z):
        nova_posicao = []
        for vertice in self.vertices:
            nova_posicao.append((vertice[0]+X, vertice[1]+Y, vertice[2]+Z))
        self.vertices = (nova_posicao)

    def mudar_raio(self,raio):
        nova_posicao = []
        contador = -1
        for vertice in self.vertices:
            contador += 1
            if (contador < 8):
                nova_posicao.append((vertice[0],vertice[1],vertice[2]))
            else:
                if (contador%4 == 0):
                    nova_posicao.append((vertice[0]-raio,vertice[1]-raio,vertice[2]))
                elif (contador%4 == 1):
                    nova_posicao.append((vertice[0]-raio,vertice[1]+raio,vertice[2]))
                elif (contador%4 == 2):
                    nova_posicao.append((vertice[0]+raio,vertice[1]+raio,vertice[2]))
                elif (contador%4 == 3):
                    nova_posicao.append((vertice[0]+raio,vertice[1]-raio,vertice[2]))
        self.vertices = (nova_posicao)
    
    



class barra():

    # base
    
    base_1 = (0.3,0.3,0)
    base_2 = (base_1[0]+0.3,base_1[1],base_1[2])
    base_3 = (base_1[0],base_1[1]+0.3,base_1[2])
    base_4 = (base_1[0]+0.3,base_1[1]+0.3,base_1[2])

    # tampa

    tampa_1 = (base_1[0],base_1[1],base_1[2]+2)
    tampa_2 = (base_2[0],base_2[1],base_2[2]+2)
    tampa_3 = (base_3[0],base_3[1],base_3[2]+2)
    tampa_4 = (base_4[0],base_4[1],base_4[2]+2)

    vertices = (
        base_1,
        base_2,
        base_3,
        base_4,
        tampa_1,
        tampa_2,
        tampa_3,
        tampa_4
        )

    edges = (
        (0,1),
        (0,2),
        (0,4),

        
        (1,3),
        (1,5),

        
        (2,6),
        (2,3),
        (3,7),

        (4,5),
        (4,6),

        (7,6),
        (7,5)

        #(5,6)
        )

    surfaces = (
            (0,2,3,1),
            (4,6,7,5),
            (0,2,6,4),
            (1,3,7,5),
            (0,1,5,4),
            (2,3,7,6)
            
        )
    
    def __init__(self, discos=[],color=[1,0,0],posicaoX=0, posicaoY=0, posicaoZ=0):
        self.discos = discos
        self.color = color
        self.x = posicaoX
        self.y = posicaoY
        self.z = posicaoZ
        if (posicaoX or posicaoY or posicaoZ):
            self.mudar_posicao(posicaoX,posicaoY,posicaoZ)
            

    def mudar_posicao(self,X,Y,Z):
        nova_posicao = []
        for vertice in self.vertices:
            nova_posicao.append((vertice[0]+X, vertice[1]+Y, vertice[2]+Z))
        self.vertices = (nova_posicao)
            
        
    def draw(self):
        # surperficie 1
        glBegin(GL_QUADS)        
        for surface in self.surfaces:
            glColor3fv((self.color[0],self.color[1],self.color[2]))
            for vertex in surface:
                glVertex3fv(self.vertices[vertex])
        glEnd();
        
                
       

def hanoi(n, source, helper, target):
    sleep(0.3)
    if n > 0:
        hanoi(n - 1, source, target, helper)
        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT);
        source.draw()
        helper.draw()
        target.draw()
        for disco in helper.discos:
            disco.draw()
        for disco in target.discos:
            disco.draw()
        for disco in source.discos:
            disco.draw()
        pygame.display.flip();
        if source.discos:
            source.discos[-1].mudar_posicao(-source.discos[-1].vertices[0][0], -source.discos[-1].vertices[0][1], -source.discos[-1].vertices[0][2])
            source.discos[-1].mudar_posicao(target.vertices[0][0],target.vertices[0][1],target.vertices[0][2]+0.1*len(target.discos))
            disco = source.discos.pop()
            target.discos.append(disco)
            glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT);
            source.draw()
            helper.draw()
            target.draw()
            contador.n+=1
            print contador.n
            for disco in helper.discos:
                disco.draw()
            for disco in target.discos:
                disco.draw()
            for disco in source.discos:
                disco.draw()
            pygame.display.flip();
            hanoi(n - 1, helper, source, target)
            glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT);
            source.draw()
            helper.draw()
            target.draw()
            for disco in helper.discos:
                disco.draw()
            for disco in target.discos:
                disco.draw()
            for disco in source.discos:
                disco.draw()
            pygame.display.flip();



def main(numero_discos):
    pygame.init();
    display = (600,600);
    pygame.display.set_mode(display, DOUBLEBUF|OPENGL);

    gluPerspective(50, (display[0]/display[1]), 0.01, 50);

    glTranslatef(-3.5,0,-20);
    glRotatef(-75,1,0,0)
    
    
    vel = 0.1;
    lista_cores = [[1,0,1],[1,0,0.5],[0.5,0.5,1],[1,1,1]]
    lista_discos = []
    for disco in range(numero_discos):
        lista_discos.append(toro_quadrado(0.1*disco,lista_cores[disco%4],1,0,0,disco*(-0.1)+numero_discos*0.1))

    
    lista_discos.reverse()

    barra_A = barra(lista_discos);
    barra_B = barra([],[0,1,0],3.3)
    barra_C = barra([],[0,0,1],6.6)

    clock = pygame.time.Clock()
    clock.tick(60);
    for event in  pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit();
            quit();


    glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT);


    barra_A.draw()
    barra_B.draw()
    barra_C.draw()
    for disco in lista_discos:
        disco.draw()
    hanoi(numero_discos,barra_A, barra_B, barra_C)
    pygame.display.flip();
    

contador = contar(0)
main(5)
