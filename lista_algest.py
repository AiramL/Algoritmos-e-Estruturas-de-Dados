#####################################################################################################################################
# Aluno: Lucas Airam Castro de Souza                                                                                                #
# Disciplina: Algoritmos e Estruturas de Dados                                                                                      #
# Professor: Edilberto Strauss                                                                                                      #
# Periodo: 2019/1                                                                                                                   #
#####################################################################################################################################


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
