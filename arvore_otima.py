

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

'''
def printar_arvore_exercicio_casa(raiz_matriz):
    i = 8
    tab = i*'\t'
    print tab+'              '+str(raiz_matriz[0][8])+'\n'
    print tab+"\t  /       \\"
    i = 8
    tab = i*'\t'   
    print tab+'       '+str(raiz_matriz[0][1])+'\t     '+str(raiz_matriz[2][8])+'\n'
    print tab+"    /     \\        /     \\"
    i = 8
    tab = i*'\t'
    print tab+'   r0'+'     '+'r1'+'    '+'r2'+'         '+str(raiz_matriz[3][8])+'\n'
    print tab+"\t\t       /       \\"
    i = 10
    tab = i*'\t'    
    print tab+'    '+str(raiz_matriz[3][5])+'            '+str(raiz_matriz[6][8])+'\n'
    print tab+" /     \\      /     \\"
    i = 9
    tab = i*'\t'
    print tab+'        r3'+'      '+str(raiz_matriz[4][5])+'    '+'r4'+'      '+str(raiz_matriz[7][8])+'\n'
    print tab+"\t     /     \\      /     \\"
    i = 10
    tab = i*'\t'
    print tab+'    r5'+'   '+'  r6'+'    '+'r7'+'   '+'  r8'+'\n'
'''    
    


if (__name__ == '__main__'):
    #print "\n\n Exercicio Aula (Slide 173)\n\n"
    encontrar_arvore_otima([0,30,5,10,0,5,30,40],[10,10,5,10,5,0,5,0])
    #print "\n\n Exercicio Para Casa \n\n"
    #K = encontrar_arvore_otima([0,10,20,10,1,2,5,2,0],[2,5,5,5,1,1,1,1,1,1])
    #print '\n\n\n'
    #print "\t\t\t\t\t\t\t\t  Arvore exercicio para casa\n\n\n"
    #printar_arvore_exercicio_casa(K)
