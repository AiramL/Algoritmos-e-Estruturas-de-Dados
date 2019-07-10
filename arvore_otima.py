

################################################################
#                                                              #
#   Lucas Airam Castro de Souza                                #
#   Universidade Federal do Rio de Janeiro                     #
#   Algoritmos e Estruturas de Dados                           #
#                                                              #
################################################################

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
    
    print "\n\t\tMatriz F"
    printar_matriz(F)
    print "\n\t\tMatriz C"
    printar_matriz(C)
    print "\n\t\tMatriz K"
    printar_matriz(K)
    return K
    


if (__name__ == '__main__'):
    encontrar_arvore_otima([0,20,30,15,15,10,5,2,1],[1,1,1,1,1,1,1,1,1])
