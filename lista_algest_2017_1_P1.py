import time
import matplotlib.pyplot

## Questao 1 ##

def contar_chamadas(posicao_serie):
    quantidade_chamadas = 0;
    quantidade_chamadas_atual = 0;
    quantidade_chamadas_anterior = 0;
    if (posicao_serie < 2):
        return 0;
    while(posicao_serie > 1):
        quantidade_chamadas = quantidade_chamadas_anterior + quantidade_chamadas_atual + 2;
        quantidade_chamadas_anterior = quantidade_chamadas_atual;
        quantidade_chamadas_atual = quantidade_chamadas;
        posicao_serie = posicao_serie - 1;

    return quantidade_chamadas;

## Questao 2 ##

def fatorar_fatoriais(entrada):
    fatoriais = 0;
    entrada = int(entrada)
    contador = 2;
    atual = 2;
    anterior = 1;
    var =entrada;
    while (entrada):
        if (entrada >= atual):
            anterior = atual;
            contador+=1;
            atual*=contador;
        else:
            fatoriais+=1;
            entrada-=anterior;
            contador = 2;
            atual = 2;
            anterior = 1;
    return fatoriais;


## Questao 3 ##

def contar_diamantes(entrada):
    atual = 0
    contador_total = 0
    contador_esquerda = 0
    while (atual < len(entrada)):
        if (entrada[atual] == "<"):
            contador_esquerda+=1
            
        if (entrada[atual] == ">" and contador_esquerda):
            contador_total+=1
            contador_esquerda-=1
        atual+=1
    return contador_total    


def obter_funcao_tempo(numero_questao, inicial=0, quantidade_testes=1000):
    resultado_i =[]
    resultado_t =[]
    if (numero_questao == 1):
        for i in range(0,quantidade_testes,10000):
            t1 = time.time()
            x = contar_chamadas(i)
            t = time.time()-t1
            resultado_i+= [i]
            resultado_t+= [t]
        matplotlib.pyplot.plot(resultado_i,resultado_t,'r--')
        matplotlib.pyplot.ylabel('Tempo (s)')
        matplotlib.pyplot.xlabel('Entrada')
        matplotlib.pyplot.show()
        

    if (numero_questao == 2):
        for i in range(inicial,quantidade_testes,10000):
            t1 = time.time()
            x = fatorar_fatoriais(i)
            t = time.time()-t1
            resultado_i+= [i]
            resultado_t+= [t]
        matplotlib.pyplot.ylabel('Tempo (s)')
        matplotlib.pyplot.xlabel('Entrada')
        matplotlib.pyplot.plot(resultado_i,resultado_t, 'o')
        matplotlib.pyplot.show()

'''
q = 4000
def obter_funcao_tempo():
    resultado_i =[]
    resultado_t =[]
    
    for i in range(q):
            t1 = time.time()
            x = contar_chamadas(i)
            t = time.time()-t1
            resultado_i+= [i]
            resultado_t+= [t]
    matplotlib.pyplot.plot(resultado_i,resultado_t, 'k')

    for i in range(q):
        t1 = time.time()
        x = fatorar_fatoriais(i)
        t = time.time()-t1
        resultado_i+= [i]
        resultado_t+= [t]
    
    matplotlib.pyplot.plot(resultado_i,resultado_t, 'r--')
    matplotlib.pyplot.show()
'''
