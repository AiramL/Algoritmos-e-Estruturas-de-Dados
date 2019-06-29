################################################################
#                                                              #
#   Lucas Airam Castro de Souza                                #
#   Universidade Federal do Rio de Janeiro                     #
#   Algoritmos e Estruturas de Dados                           #
#                                                              #
################################################################

class arvore_binaria():
    def __init__(self,dado=0,p=0,fe=0,fd=0):
        self.p = p
        self.dado=dado
        self.fe=fe
        self.fd=fd




'''
    def rot_s_d(self):
        u = self.fe
        p = self
        p.fe = u.fd
        p.p = u
        u.fd = p
        self.dado = u.dado
        self.fd = u.fd
        self.fe = u.fe
        self.fd.c -= 1       # definir novas alturas
        self.fe.c += 1
        self.c = MAX(self.fe.c,self.fd.c) + 1
        self.ce = self.fe.c
        self.cd = self.fd.c
  '''        
class arvore_avl():
    def __init__(self,p=0,dado="-",fe=0,fd=0,c=0,ce=0,cd=0):
        self.p = p
        self.dado=dado
        self.fe=fe
        self.fd=fd
        self.c=c
        self.ce=ce
        self.cd=cd

    # Rotacao simples direita
    def rot_s_d(self):
        p = arvore_avl(self.fe,self.dado,self.fe.fd,self.fd,MAX(self.fd.c,self.fe.fd.c)+1,self.fe.fd.c,self.fd.c)
        u = arvore_avl(None,self.fe.dado,self.fe.fe,p,MAX(self.fe.fe.c,p.c)+1,self.fe.fe.c,p.c)
        return u
        
      
    # Rotacao simples esquerda
    def rot_s_e(self):
        p = arvore_avl(self.fd,self.dado,self.fe,self.fd.fe,MAX(self.fe.c,self.fd.fe.c)+1,self.fe.c,self.fd.fe.c)
        u = arvore_avl(None,self.fd.dado,p,self.fd.fd,MAX(self.fd.fd.c,p.c)+1,self.fd.fd.c,p.c)
        return u

    # Rotacao dupla esquerda
    def rot_du_e(self): 
        p = arvore_avl(self.fd.fe,self.dado,self.fe,self.fd.fe.fe,MAX(self.fe.c,self.fd.fe.fe.c)+1,self.fe.c,self.fd.fe.fe.c)
        u = arvore_avl(self.fd.fe,self.fd.dado,self.fd.fe.fd,self.fd.fd,MAX(self.fd.fe.fd.c,self.fd.fd.c)+1,self.fd.fe.fd.c,self.fd.fd.c)
        v = arvore_avl(None,self.fd.fe.dado,p,u,MAX(u.c,p.c)+1,p.c,u.c)
        return v


    # Rotacao dupla direita
    def rot_du_d(self):
        p = arvore_avl(self.fe.fd,self.dado,self.fe.fd.fd,self.fd,MAX(self.fe.fd.fd.c,self.fd.c)+1, self.fe.fd.fd.c,self.fd.c)
        u = arvore_avl(self.fe.fd,self.fe.dado,self.fe.fe,self.fe.fd.fe,MAX(self.fe.fe.c,self.fe.fd.fe.c)+1,self.fe.fe.c,self.fe.fd.fe.c)
        v = arvore_avl(None,self.fe.fd.dado,u,p,MAX(u.c,p.c)+1,u.c,p.c)
        return v



def MAX(x,y):
    if (x > y):
        return x
    return y
    

def tornar_avl(raiz):
    
    if (raiz.fe.dado != "-"):
        raiz.fe = tornar_avl(raiz.fe) # Balancear filho esquerdo
        


    if (raiz.fd.dado != "-"):
        raiz.fd = tornar_avl(raiz.fd) # Balancear filho direito

    raiz.ce = raiz.fe.c               # Obter altura filho esquerdo
    raiz.cd = raiz.fd.c               # Obter altura filho direito


    ######################### Definir tipo de rotacao se necessario ####################
    
    if((raiz.ce - raiz.cd > 1)):
        if(raiz.fe.fe.c >= raiz.fe.fd.c):
            raiz = raiz.rot_s_d()
        else:
            raiz = raiz.rot_du_d()
                
    if ((raiz.cd - raiz.ce > 1)):
        if(raiz.fd.cd >= raiz.fd.ce):
            raiz = raiz.rot_s_e()
            
        else:
            raiz = raiz.rot_du_e()
                    
    ####################################################################################


        
    ########################## Arvore ja eh AVL, definir altura ########################
    
    else:       
        raiz.c = MAX(raiz.fe.c,raiz.fd.c) + 1

    
    ####################################################################################

    return raiz # Raiz da arvore balanceada



def printar_matriz(matriz):
    print '\n'
    for i in matriz:
        linha = ""
        for j in i:
            l = str(j)
            linha+=l.center(5)
        print linha

def criar_matriz(n,m):
    matriz = []
    for i in range(n):
        linha = []
        for j in range(m):
            linha+=['-']
        matriz+=[linha]
    return matriz
        
def criar_matriz_quadrada(n):
    return criar_matriz(n,n)
    


def custo_minimo(i,j):
    minimo = 0
    for k in range(1,j+1):
        custo = C[i][k-1] + C[k][j]
        if (custo < minimo) or (K[i][j] == 0):
            minimo = custo
            K[i][j] = k
    return minimo



def encontrar_arvore_otima(frequencia_j,frequencia_j_linha):
    n = len(frequencia_j);
    K = criar_matriz_quadrada(n);
    F = criar_matriz_quadrada(n);
    C = criar_matriz_quadrada(n);
    for j in range(n):
        F[j][j] = frequencia_j_linha[j]
        C[j][j] = 0
    for d in range(1,n+1):
        for i in range(n-d):
            j = i + d
            F[i][j] = F[i][j-1] + frequencia_j[j] + frequencia_j_linha[j]
            minimo = C[i][i] + C[i+1][j]
            for k in range(i+1,j+1):
                custo = C[i][k-1] + C[k][j]
                if (custo <= minimo):
                    minimo = custo
                    K[i][j] = k
            C[i][j] = minimo + F[i][j]
    return K

    
def montar_arvore_otima(matrix,i,j,pai):
    k = matrix[i][j]
    raiz = arvore_avl(pai,k,arvore_avl(),arvore_avl())
    if (k != "-"):
        raiz.fe = montar_arvore_otima(matrix,i,k-1,raiz)
        raiz.fd = montar_arvore_otima(matrix,k,j,raiz)
    return raiz

if (__name__ == '__main__'):
    mat = encontrar_arvore_otima([0,30,5,10,0,5,30,40],[10,10,5,10,5,0,5,0])
    av = montar_arvore_otima(mat,0,7,None)
    x = tornar_avl(av)
    print "nivel 1 ----> "+str(x.dado)
    print "nivel 2 ----> "+str(x.fe.dado)+"     "+str(x.fd.dado)
    print "nivel 3 ----> "+str(x.fe.fe.dado)+"     "+str(x.fe.fd.dado)+"   "+str(x.fd.fe.dado)+"     "+str(x.fd.fd.dado)
    print "nivel 4 ----> "+str(x.fe.fd.fe.dado)+"     "+str(x.fe.fd.fd.dado)+"   "+str(x.fd.fe.fe.dado)+"     "+str(x.fd.fe.fd.dado)+"    "+str(x.fd.fd.fe.dado)+"    "+str(x.fd.fd.fd.dado)
    
    
