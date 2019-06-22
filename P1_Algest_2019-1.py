# -*- coding: cp1252 -*-
#####################################################################################################################################
# Aluno: Lucas Airam Castro de Souza                                                                                                #
# Disciplina: Algoritmos e Estruturas de Dados                                                                                      #
# Professor: Edilberto Strauss                                                                                                      #
# Periodo: 2019/1                                                                                                                   #
#####################################################################################################################################





############################################################ Questao 1 ##############################################################



class pilha():                                 # declaracao da estrutura de dado do tipo pilha
    def __init__(self,topo=[]):
        self.topo = topo

    def retirar(self):                         # retirar um elemento do topo da pilha
        if (len(self.topo)):
            item = self.topo[0];
            self.topo = self.topo[1:];
            return item;
        
    def inserir(self, novo):                    # inserir um novo elemento na pilha
        self.topo.insert(0,novo);

def ehOperando(caracter):                       # verificar se elemento eh um operando, so aceita letras como operandos
    if (caracter in "abcdefghijklmnopqrstuwvxyzABCDEFGHIJKLMNOPQRSTUWVXYZ"):
        return True
    return False

def ehOperador(caracter):                       # verificar se elemento eh um operador
    if (caracter in ["/","*","+","-","^","(",")"]):
        return True;
    return False;

def prioridade(operador_1, operador_2):         # verificar qual a prioridade entre os operadores, retorna 1 caso operador 1 tenha maior prioridade
    prioridade_operador_1 = 0;
    prioridade_operador_2 = 0;
    if(operador_1 == '^'):
       prioridade_operador_1 = 4;
    elif((operador_1 == '*') or (operador_1 == '/')):
       prioridade_operador_1 = 2;        
    elif(operador_1 == '+' or operador_1 == '-'):
       prioridade_operador_1 = 1;
    elif(operador_1 == '('):
       prioridade_operador_1 = 4;
    if(operador_2 == '^'):
       prioridade_operador_2 = 3;
    elif(operador_2 == '*' or operador_2 == '/'):
       prioridade_operador_2 = 2;
    elif(operador_2 == '+' or operador_2 == '-'):
       prioridade_operador_2 = 1;
    elif(operador_2 == '('):
       prioridade_operador_2 = 0;
    return (prioridade_operador_1 > prioridade_operador_2);
        



def converte_in_pos(infixa_lista):
    pilha_pos = pilha([]);                  # apesar da declaracao ser do tipo pilha, essa estrutura eh utilizada como uma fila
    pilha_operador = pilha([]);             # pilha de operadores da expressao de entrada
    contador = 0;
    elemento = "";
    while(len(infixa_lista) > contador):
        operador = "";
        elemento = infixa_lista[contador];
        contador += 1;
        if (ehOperando(elemento)):
            pilha_pos.inserir(elemento);
        elif (elemento == "("):
            pilha_operador.inserir(elemento);
        elif (elemento == ")" or ((len(infixa_lista) - contador) == 0)):
            operador = pilha_operador.retirar();
            if (operador != "("):
                pilha_pos.inserir(operador);
            while (operador != "("):
                operador = pilha_operador.retirar();
                if (operador != "("):
                    pilha_pos.inserir(operador);
        elif(ehOperador(elemento)):
            while(operador != None):
                operador = pilha_operador.retirar();
                if (operador != None):
                    if (prioridade(elemento,operador)):
                        pilha_operador.inserir(operador);
                        pilha_operador.inserir(elemento);
                        break;
                    else:
                        pilha_pos.inserir(operador);
                else:
                    pilha_operador.inserir(elemento);
    while (pilha_operador.topo != []):
        operador = pilha_operador.retirar();
        if (operador != None):
            pilha_pos.inserir(operador);
    elemento = "";
    operador = "";
    while(True):
        if pilha_pos.topo != []:
            operador = pilha_pos.topo.pop();
            elemento+=operador;
        else:
            break
    return elemento;



############################################################## Fim Questao 1 ########################################################



############################################################ Questao 2 ##############################################################



#####################################################################################################################################
#                                                                                                                                   #
#  A estrutura de dados definada para o problema, e que ajuda a chegar no algoritmo otimo sao as classes abaixo. Assumesse que o no #
#  grid mestre eh desconhecido, um problema de busca dessa natureza, similar ao problema da celebridade eh de natureza n, visto que #
#  para conhecermos o grid master devemos passar por todos os nos no pior caso.                                                     #
#                                                                                                                                   #
#  As estruturas sao diferentes pois as funcoes do no grid master sao diferentes das funcoes realizadas por nos comuns. Ambas       #
#  estruturas possuem uma flag indicando se o no eh o grid master ou nao. Todos os nos estao conectados por um lista encadeada,     #
#  indicada por "proximo". Para o no grid, ele possui o endereco do primeiro no da rede, ja que ele conhece todos os nos, pode      #
#  navegar por todda a lista encadeada.                                                                                             #
#                                                                                                                                   #
#  Os nos comuns possuem uma lista de nos conhecidos. Eles nao conhecem necessariamente todos os nos da rede, logo essa lista so    #
#  leva a conjunto que eh menor ou igual que a lista de nos da rede.                                                                #
#                                                                                                                                   #
#  Para descobrir quem eh o no grid master bastas percorrer todos os proximos, com um laco de repeticao, testando a flag de grid.   #
#  Quando encontrar a flag em 1 significa que aquele no eh o no grid master.                                                        #
#                                                                                                                                   #
#  O laco de repeticao leva a uma complexidade n do algoritmo, como n eh tambem o omega do problema, o algoritmo eh dito otimo.     #
#                                                                                                                                   #
#####################################################################################################################################

class grid_comum():
    def __init__(self, proximo, primeiro, grid=0):
        self.grid = grid;
        self.proximo = proximo
        self.lista_conhecidos = primeiro;
    # funcoes nao grid 


        
class grid_master():
    def __init__(self,proximo,primeiro, grid=1):
        self.grid = grid;
        self.lista_maquinas = primeiro
        self.proximo = proximo
    # funcoes grid gerenciamento

###################################################### Fim Questao 2 ###############################################################################






########################################################### Questao 3 ##############################################################################

class arvore():                                                             # definicao de uma estrutura de arvore
    def __init__(self, pai=None, dado=None, esquerda=None, direita=None):
        self.dado = dado;
        self.pai = pai;
        self.filho_direito = direita;
        self.filho_esquerdo = esquerda;

        


################################################# Solucao para montar a arvore #####################################################################
#                                                                                                                                                  #
# A complexidade do algoritmo eh nlog(n), pois estamos fazendo n chamadas recursivas da funcao, porem estamos cada vez mais diminuindo a entrada,  #
# num processo continuo de divisao por 2, tendo um comportamento nao linear, logaritmico. Como a natureza do problema eh igual ao O, algoritmo eh  #
# otimo                                                                                                                                            #
#                                                                                                                                                  #
####################################################################################################################################################



def montar_arvore(pre,sim,pai):
    if len(pre) > 0:
        metade = sim.index(pre[0])
        pre_e = pre[1:(len(pre)/2)+1]
        pre_d = pre[len(pre)/2+1:]
        sim_e = sim[:metade]
        sim_d = sim[metade+1:]
        raiz = arvore(pai,pre[0],None,None);
        raiz.filho_esquerdo =  montar_arvore(pre_e,sim_e,raiz)
        raiz.filho_direito =  montar_arvore(pre_d,sim_d,raiz)
        return raiz
    else:
        return arvore()


def retornar_pos(arvore):                                # a funcao recebe a raiz de uma arvore e retorna a arvore em pos ordem
    lista_pos = ''
    if(arvore.filho_esquerdo != None):
        lista_pos+=retornar_pos(arvore.filho_esquerdo);
        
    if(arvore.filho_direito != None):
        lista_pos+=retornar_pos(arvore.filho_direito);
    if (arvore.dado != None):
        lista_pos += arvore.dado;
    return lista_pos;

def resolucao(pre,sim):                                     # a funcao junta outras duas funcoes para devolver a resposta da questao
    resposta = retornar_pos(montar_arvore(pre,sim,None));
    return resposta

############################################################### Fim Questao 3 ########################################################

if (__name__ == "__main__"):
    print "Questao 1"
    print "entrada: a-b \t\t\t resposta: "+str(converte_in_pos('a-b'))
    print "entrada: a-b*c \t\t\t resposta: "+str(converte_in_pos('a-b*c'))
    print "entrada: (a-b)*c \t\t resposta: "+str(converte_in_pos('(a-b)*c'))
    print "entrada: a+b*c^d-e \t\t resposta: "+str(converte_in_pos('a+b*c^d-e'))
    print "entrada: a*(b+c)*(d-g)*h \t resposta: "+str(converte_in_pos('a*(b+c)*(d-g)*h'))
    print "entrada: a*b-c*d^e/f+g*h \t resposta: "+str(converte_in_pos('a*b-c*d^e/f+g*h'))
    print '\n\nQuestao 2 nao possui resultado exibivel'
    print "\n\nQuestao 3"
    print "entrada: abc, bac \t\t resposta: "+str(resolucao("abc","bac"))
    print "entrada: 7546980,4567890 \t resposta: "+str(resolucao ("7546980","4567890"))

