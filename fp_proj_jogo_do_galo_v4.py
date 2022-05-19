#Tiago Alexandre Pereira Antunes   99331


    
def eh_tabuleiro(t):
    '''
    universal --> booleano
    predicado que apenas devolve True se o argumento for um tabuleiro
    '''
    if not (type(t) == tuple):                                               #isinstance(t, tuple):
        return False
    elif len(t) != 3:
        return False
    elif not (type(t[0]) == tuple and type(t[1]) == tuple and \
              type(t[2]) == tuple):                                         #(isinstance(t[0], tuple) and isinstance(t[1], tuple) and isinstance(t[2], tuple)):
        return False
    elif len(t[0]) != 3  or len(t[1]) != 3 or len(t[2]) != 3:
        return False
    else:
        for i in t:
            for n in range(len(i)):
                if not (type(i[n]) == int and i[n] in (-1, 0, 1)):
                    return False
        return True
    
def eh_posicao(n):
    '''
    universal --> booleano
    predicado que apenas devolve True se o seu argumento corresponder a uma
    posicao
    '''
    if type(n) == int:
        if n in (1,2,3,4,5,6,7,8,9):
            return True
        else:
            return False
    else:
        return False
    
    
def obter_coluna(tabuleiro, n):
    '''
    tabuleiro x inteiro --> vector
    recebe um tabuleiro e um numero entre 1 e 3 e retorna a coluna
    correspondente a esse numero
    '''
    if eh_tabuleiro(tabuleiro) == True and n in (1, 2, 3):
        coluna = ()
        for i in range(len(tabuleiro)):
            coluna = coluna + (tabuleiro[i][n - 1], )

    else:
        raise ValueError('obter_coluna: algum dos argumentos e invalido')
    
    return coluna

def obter_linha(tabuleiro, n):
    '''
    tabuleiro x inteiro --> vector
    recebe um tabuleiro e um numero entre 1 e 3 e retorna a linha correspondente
    a esse numero
    '''
    if eh_tabuleiro(tabuleiro) == True and type(n) == int and n in (1, 2, 3):
        return tabuleiro[n - 1]

    else:
        raise ValueError('obter_linha: algum dos argumentos e invalido')
    
    
def obter_diagonal(tabuleiro, n):
    '''
    tabuleiro x inteiro --> vector
    recebe um inteiro e um numero entre 1 e 2 e retorna a diagonal
    correspondente a esse numero 
    '''
    if eh_tabuleiro(tabuleiro) == True and type(n) == int and n in (1, 2):
        if n == 1:
            diagonal = (tabuleiro[0][0], tabuleiro[1][1], tabuleiro[2][2])
               
        else:
            diagonal = (tabuleiro[2][0], tabuleiro[1][1], tabuleiro[0][2]) 
        
    else:
        raise ValueError('obter_diagonal: algum dos argumentos e invalido')
    
    return diagonal


def tabuleiro_str(tabuleiro):
    '''
    tabuleiro --> cadeia de caracteres
    recebe um tabuleiro e devolve a cadeia de caracteres que o representa
    '''
    if eh_tabuleiro(tabuleiro) == True:
        tab = ''
        for i in range(len(tabuleiro)):
            linha = tabuleiro[i]
            for n in range(len(linha)):
                if linha[n] == 1:
                    if n == 0 or n == 1:
                        tab = tab + ' X |'   #adicionar | se for a coluna 1 ou 2
                    else:
                        tab = tab + ' X '    
                    
                elif linha[n] == -1:
                    if n == 0 or n == 1:
                        tab = tab + ' O |'
                    else:
                        tab = tab + ' O '                   
                    
                else:
                    if n == 0 or n == 1:
                        tab = tab + '   |'
                    else:
                        tab = tab + '   '                    
            if i != 2:                          #se nao for a ultima linha 
                tab = tab + '\n-----------\n'   #meter a divisoria 
    else:
        raise ValueError('tabuleiro_str: o argumento e invalido')
    
    return tab


def eh_posicao_livre(tabuleiro, pos):
    '''
    tabuleiro x posicao --> booleano
    predicado que apenas devolve se a posicao corresponder a uma posicao livre
    do tabuleiro
    '''
    if eh_tabuleiro(tabuleiro) == True and eh_posicao(pos) == True:
        dict = {1 : tabuleiro[0][0], 2 : tabuleiro[0][1], 3 : tabuleiro[0][2], \
                4 : tabuleiro[1][0], 5 : tabuleiro[1][1], 6 : tabuleiro[1][2], \
                7 : tabuleiro[2][0], 8 : tabuleiro[2][1], 9 : tabuleiro[2][2]}        
        if dict[pos] == 0:
            return True
        
        return False
    
    else:
        raise ValueError('eh_posicao_livre: algum dos argumentos e invalido')
        

def obter_posicoes_livres(tabuleiro):
    '''
    tabuleiro --> vector
    recebe um tabuleiro e devolve um vector ordendo com todas as posicoes livres
    do tabuleiro
    '''
    if eh_tabuleiro(tabuleiro) == True:
        dict = {1 : tabuleiro[0][0], 2 : tabuleiro[0][1], 3 : tabuleiro[0][2], \
                4 : tabuleiro[1][0], 5 : tabuleiro[1][1], 6 : tabuleiro[1][2], \
                7 : tabuleiro[2][0], 8 : tabuleiro[2][1], 9 : tabuleiro[2][2]}    
        pos_livres = ()
        for pos in dict:
            if dict[pos] == 0:
                pos_livres = pos_livres + (pos, )
        return pos_livres
    
    else:
        raise ValueError('obter_posicoes_livres: o argumento e invalido')
                
                
def jogador_ganhador(tabuleiro):
    '''
    tabuleiro --> inteiro
    recebe um tabuleiro e devolve um inteiro a indicar o jogador que venceu
    a partida
    '''
    if eh_tabuleiro(tabuleiro) == True:
        for n in (1, 2, 3):
            l = obter_linha(tabuleiro, n)
            c = obter_coluna(tabuleiro, n)
            if l == (1, 1, 1) or c == (1, 1, 1):
                return 1
            
            elif l == (-1, -1, -1) or c == (-1, -1, -1):
                return -1
            
        for n in (1, 2):
            d = obter_diagonal(tabuleiro, n)
            if d == (1, 1, 1):
                return 1
            
            elif d == (-1, -1, -1):
                return -1
            
        return 0  
        
    else:
        raise ValueError('jogador_ganhador: o argumento e invalido')
    
def marcar_posicao(tabuleiro, i, pos):
    '''
    tabuleiro x inteiro x posicao --> tabuleiro
    recebe um tabuleiro, um inteiro identificando o jogador e um posicao livre
    e devolve o tabuleiro com a marca do jogador nessa posicao
    '''
    if eh_tabuleiro(tabuleiro) == True and type(i) == int and i in (1, -1)\
       and eh_posicao(pos) == True:
        if type(pos) == int and eh_posicao_livre(tabuleiro, pos) == True:
            tab = ()
                
            dict = posicoes(tabuleiro)   
            
            dict[pos] = i                 #meter na posicao o numero do jogador
            
            linha1 = ()
            linha2 = ()
            linha3 = ()
            
            for c in dict:
                if c < 4:
                    linha1 = linha1 + (dict[c], )
                elif c > 3 and c < 7:
                    linha2 = linha2 + (dict[c], )
                else:
                    linha3 = linha3 + (dict[c], )
                    
            tab = (linha1, linha2, linha3)
                
            return tab
        else: 
            raise \
             ValueError('marcar_posicao: algum dos argumentos e invalido')            
    else:
        raise \
         ValueError('marcar_posicao: algum dos argumentos e invalido')

#-------------------------------------------------------------------------------        
# funcoes de jogo

def escolher_posicao_manual(tabuleiro):
    '''
    tabuleiro --> posicao
    le a posicao introduzida por um jogador e retorna essa posicao
    '''
    if eh_tabuleiro(tabuleiro) == True:                 
        pos = eval(input('Turno do jogador. Escolha uma posicao livre: '))
        if pos in obter_posicoes_livres(tabuleiro):
            return pos
            
        else:
            raise ValueError(\
                'escolher_posicao_manual: a posicao introduzida e invalida')
        
    else:
        raise ValueError('escolher_posicao_manual: o argumento e invalido')
    
    
    
def escolher_posicao_auto(tabuleiro, n, cc):
    '''
    tabuleiro x inteiro x cad.caracteres --> posicao
    recebe um tabuleiro, um inteiro indentificando o jogador e uma cadeia de
    caracteres correspondente a estrategia e devolve a posicao escolhida 
    automaticamente de acordo com a estrategia
    '''
    if eh_tabuleiro(tabuleiro) == True and type(n) == int and n in (-1, 1) and \
       type(cc) == str and cc in ('basico', 'normal', 'perfeito'):
        if cc == 'basico':
            if centro(tabuleiro) != ():       #realizar as estrategias por ordem
                return 5
            elif canto_vazio(tabuleiro) != ():
                pos = canto_vazio(tabuleiro)
                return pos[0]
            elif lateral_vazio(tabuleiro) != 0:
                pos = lateral_vazio(tabuleiro)
                return pos[0]
                
        elif cc == 'normal':        
            tab = ((1,2,3),(4,5,6),(7,8,9))
            if vitoria(tabuleiro, n) != ():
                pos_ord = ordenar_posicoes(vitoria(tabuleiro, n))
                return pos_ord[0]
            elif bloqueio(tabuleiro, n) != ():
                pos_ord = ordenar_posicoes(bloqueio(tabuleiro, n))
                return pos_ord[0]
            elif centro(tabuleiro) != ():
                return 5
            elif canto_oposto(tabuleiro, n) != ():
                pos_ord = ordenar_posicoes(canto_oposto(tabuleiro, n))
                return pos_ord[0]                
            elif canto_vazio(tabuleiro) != ():
                pos = canto_vazio(tabuleiro)
                return pos[0]
            elif lateral_vazio(tabuleiro) != 0:
                pos = lateral_vazio(tabuleiro)
                return pos[0]
            
        elif cc == 'perfeito':
            tab = ((1,2,3),(4,5,6),(7,8,9))
            if vitoria(tabuleiro, n) != ():
                pos_ord = ordenar_posicoes(vitoria(tabuleiro, n))
                return pos_ord[0]
            elif bloqueio(tabuleiro, n) != ():
                pos_ord = ordenar_posicoes(bloqueio(tabuleiro, n))
                return pos_ord[0]
            elif bifurcacao(tabuleiro, n) != ():
                pos_ord = ordenar_posicoes(bifurcacao(tabuleiro, n))
                return pos_ord[0]            
            elif bloqueio_bifurcacao(tabuleiro, n) != ():
                pos_ord = ordenar_posicoes(bloqueio_bifurcacao(tabuleiro, n))
                return pos_ord[0]            
            elif centro(tabuleiro) != ():
                return 5
            elif canto_oposto(tabuleiro, n) != ():
                pos_ord = ordenar_posicoes(canto_oposto(tabuleiro, n))
                return pos_ord[0]                
            elif canto_vazio(tabuleiro) != ():
                pos = canto_vazio(tabuleiro)
                return pos[0]
            elif lateral_vazio(tabuleiro) != 0:
                pos = lateral_vazio(tabuleiro)
                return pos[0]            
    else:
        raise \
          ValueError('escolher_posicao_auto: algum dos argumentos e invalido')
 
 
def jogo_do_galo(c_jogador, cc):
    '''
    cad. caracteres x cad. caracteres --> tabuleiro
    recebe um cad. caracteres que indentifica o jogador humano e outra
    estrategia para o computador e devolve o tabuleiro depois de cada jogada
    e acaba quando um ganhar ou quando nao houver espaco disponivel no tabuleiro
    '''
    if c_jogador in ('X', 'O') and cc in ('basico', 'normal', 'perfeito'):
        tabuleiro = ((0,0,0),(0,0,0),(0,0,0))
        if c_jogador == 'O':
            print("Bem-vindo ao JOGO DO GALO.\nO jogador joga com 'O'.")
        elif c_jogador == 'X':
            print("Bem-vindo ao JOGO DO GALO.\nO jogador joga com 'X'.")
        while jogador_ganhador(tabuleiro) == 0 and \
              obter_posicoes_livres(tabuleiro) != ():
            if c_jogador == 'O':
                pos_auto = escolher_posicao_auto(tabuleiro, 1, cc)
                tabuleiro = marcar_posicao(tabuleiro, 1, pos_auto)
                print('Turno do computador', '(' + cc + '):')
                print(tabuleiro_str(tabuleiro))
                end = end_game(tabuleiro)
                if end != '':
                    return end                                
                
                pos_jog = escolher_posicao_manual(tabuleiro)
                tabuleiro = marcar_posicao(tabuleiro, -1, pos_jog)
                print(tabuleiro_str(tabuleiro))
                end = end_game(tabuleiro)
                if end != '':
                    return end

            elif c_jogador == 'X':
                pos_jog = escolher_posicao_manual(tabuleiro)
                tabuleiro = marcar_posicao(tabuleiro, 1, pos_jog)
                print(tabuleiro_str(tabuleiro))
                end = end_game(tabuleiro)
                if end != '':
                    return end                
                pos_auto = escolher_posicao_auto(tabuleiro, -1, cc)
                tabuleiro = marcar_posicao(tabuleiro, -1, pos_auto)
                print('Turno do computador', '(' + cc + '):')
                print(tabuleiro_str(tabuleiro))
                end = end_game(tabuleiro)
                if end != '':
                    return end                
    else:
        raise ValueError('jogo_do_galo: algum dos argumentos e invalido')
#-------------------------------------------------------------------------------
# Aux

def posicoes(tab):
    '''
    faz um dicionario com as posicoes como chaves para os numeros no tabuleiro
    '''
    dict = {1 : tab[0][0], 2 : tab[0][1], 3 : tab[0][2], \
            4 : tab[1][0], 5 : tab[1][1], 6 : tab[1][2], \
            7 : tab[2][0], 8 : tab[2][1], 9 : tab[2][2]}   
    
    return dict


def end_game(tabuleiro):
    '''
    tabuleiro --> cad. caracteres
    receb um tabuleiro e retorna uma cad_caracteres identificando o jogador que
    ganhou ou que houve empate ou que o jogo ainda esta a decorrer
    '''
    if jogador_ganhador(tabuleiro) == 1:
        return 'X'
    elif jogador_ganhador(tabuleiro) == -1:  
        return 'O'
    elif obter_posicoes_livres(tabuleiro) == ():    
        if jogador_ganhador(tabuleiro) == 0:
            return 'EMPATE'
    else:
        return ''


def ordenar_posicoes(tuplo):
    '''
    recebe um tuplo com as possiveis posicoes de jogo e ordena-as para que na
    primeira posicao fique a mais pequena
    '''
    ord_pos = list(tuplo)
    maior_indice = len(ord_pos) - 1
    nenhuma_troca = False
    while not nenhuma_troca:
        nenhuma_troca = True
        for i in range(maior_indice):
            if ord_pos[i] > ord_pos[i+1]:
                ord_pos[i], ord_pos[i+1] = ord_pos[i+1], ord_pos[i]
                nenhuma_troca = False
        maior_indice = maior_indice - 1
            
    return ord_pos    

#-------------------------------------------------------------------------------
# basico

def centro(tabuleiro):
    '''
    tabuleiro --> posicao
    recebe um tabuleiro e devolve a posicao caso esteja disponivel 
    '''
    if eh_tabuleiro(tabuleiro) == True:
        res = ()
        if 5 in obter_posicoes_livres(tabuleiro):        #centro
            res = res + (5, )
        return res
    else:
        raise ValueError('centro: argumento invalido')

def canto_vazio(tabuleiro):
    '''
    tabuleiro --> tuplo
    recebe um tabuleiro e devolve um tuplo com todas as posicoes dos cantos
    livres
    '''
    if eh_tabuleiro(tabuleiro) == True:
        res = ()
        for i in (1, 3, 7, 9):
            if i in obter_posicoes_livres(tabuleiro):    #canto vazio
                res = res + (i, )  
        return res

    else:
        raise ValueError('canto_vazio: argumento invalido')
    
def lateral_vazio(tabuleiro):
    '''
    tabuleiro --> tuplo
    recebe um tabuleiro e devolve um tuplo com todas as posicoes laterais
    que nao sao cantos e estao livres
    '''
    if eh_tabuleiro(tabuleiro) == True:
        res = ()
        for i in (2, 4, 6, 8):                          #lateral vazio
            if i in obter_posicoes_livres(tabuleiro):
                res = res + (i, )  
        return res
    else:
        raise ValueError('lateral_vazio: argumento invalido')


#------------------------------------------------------------------------------
# normal

def vitoria(tabuleiro, n):
    '''
    tabuleiro x inteiro --> tuplo
    recebe um tabuleiro e devolve um tuplo com todas as posicoes livres onde
    o jogador identificado pelo inteiro pode jogar de forma a ganhar o jogo
    '''
    if eh_tabuleiro(tabuleiro) == True and n in (-1, 1):
        tab = ((1,2,3),(4,5,6),(7,8,9))
        res = ()
        for l in (1, 2, 3):
            linha = obter_linha(tabuleiro, l)
            coluna = obter_coluna(tabuleiro, l)
            if linha == (n, n, 0) or linha == (n, 0, n) or \
               linha == (0, n, n):
                for i in range(len(linha)):
                    if linha[i] == 0:
                        res = res + (tab[l-1][i], )
                    
            if coluna == (n, n, 0) or coluna == (n, 0, n) or  \
               coluna == (0, n, n):
                for i in range(len(coluna)):
                    if coluna[i] == 0:
                        res = res + (tab[i][l-1], )
                    
        for d in (1, 2):
            diagonal = obter_diagonal(tabuleiro, d)
            if diagonal == (n, n, 0) or diagonal == (n, 0, n) or \
               diagonal == (0, n, n):
                for i in range(len(diagonal)):
                    if diagonal[i] == 0:
                        if i == 0:
                            if d == 1:
                                res = res + (tab[0][0], )
                            elif d == 2:
                                res = res + (tab[2][0], )
                            
                        elif i == 1:
                            if tab[1][1] not in res:
                                res = res + (tab[1][1], )
                            
                        
                        elif i == 2:  
                            if d == 2:
                                res = res + (tab[0][2], )
                            elif d == 1:
                                res = res + (tab[2][2], ) 
        return res
         
    else:
        raise ValueError('vitoria: um dos arguentos e invalido')
                     
            
            
def bloqueio(tabuleiro, n):
    '''
    tabuleiro x inteiro --> tuplo
    recebe um tabuleiro e devolve um tuplo com as posicoes livres onde o jogador 
    identificado pelo inteiro pode jogar para bloquear a vitoria do outro
    '''
    if eh_tabuleiro(tabuleiro) == True and n in (-1, 1):
        tab = ((1,2,3),(4,5,6),(7,8,9))
        res = ()
        s = 0 - n
        for l in (1, 2, 3):
            linha = obter_linha(tabuleiro, l)
            coluna = obter_coluna(tabuleiro, l)
            if linha == (s, s, 0) or linha == (s, 0, s) or \
               linha == (0, s, s):
                for i in range(len(linha)):
                    if linha[i] == 0:
                        res =  res + (tab[l-1][i], )
                    
            if coluna == (s, s, 0) or coluna == (s, 0, s) or  \
               coluna == (0, s, s):
                for i in range(len(coluna)):
                    if coluna[i] == 0:
                        res = res + (tab[i][l-1], )
                    
        for d in (1, 2):
            diagonal = obter_diagonal(tabuleiro, d)
            if diagonal == (s, s, 0) or diagonal == (s, 0, s) or \
               diagonal == (0, s, s):
                for i in range(len(diagonal)):
                    if diagonal[i] == 0:
                        if i == 0:
                            if d == 1:
                                res = res + (tab[0][0], )
                            elif d == 2:
                                res = res + (tab[2][0], )
                            
                        elif i == 1:
                            res = res + (tab[1][1], )
                            
                        
                        elif i == 2:  
                            if d == 2:
                                res = res + (tab[0][2], )
                            elif d == 1:
                                res = res + (tab[2][2], )
                                
        return res
                            
    else:
        raise ValueError('bloqueio: um dos argumentos e invalido')
                        
                        
def canto_oposto(tabuleiro, n):
    '''
    tabuleiro x inteiro --> tuplo
    recebe um tabuleiro e devolve um tuplo com as posicoes livres diagonalmente
    opostas a marcas do jogador oposto que estejam nos cantos
    '''
    if eh_tabuleiro(tabuleiro) == True and n in (-1, 1):   
        res = ()
        dici = posicoes(tabuleiro)
        s = 0 - n
        if dici[9] == s and dici[1] == 0:
            res = res + (1, )
        elif dici[7] == s and dici[3] == 0:
            res = res + (3, )
        elif dici[3] == s and dici[7] == 0:
            res = res + (7, )
        elif dici[1] == s and dici[9] == 0:
            res = res + (9, )
            
        return res
    else:
        raise ValueError('canto_oposto: um dos argumentos e invalido')
    
#-------------------------------------------------------------------------------
# perfeito


def bifurcacao(tabuleiro, n):
    '''
    tabuleiro x inteiro --> tuplo
    recebe um tabuleiro e devolve o tuplo com as posicoes de intersecao livres
    entre duas linhas/colunas/diagonais que tenham pelo menos uma peca do
    jogador identificado pelo inteiro
    '''
    if eh_tabuleiro(tabuleiro) == True and n in (-1, 1):
        tab = ((1,2,3),(4,5,6),(7,8,9))
        res = ()
        for l in range(len(tabuleiro)):
            if n in tabuleiro[l]:
                dici = posicoes(tabuleiro)
                for c in (1, 2, 3):
                    coluna = obter_coluna(tabuleiro, c)
                    if n in coluna and (0-n) not in tabuleiro[l] and \
                       (0-n) not in coluna:
                        pos = tab[l][c-1]
                        if dici[pos] == 0:
                            res = res + (tab[l][c-1], )
                    
                    if n in coluna and (0-n) not in coluna:
                        for d in (1, 2):
                            diagonal = obter_diagonal(tabuleiro, d)
                            if (0-n) not in diagonal:
                                if n in diagonal and d == 1:
                                    if c == 1 and diagonal[c-1] == 0:
                                        res = res + (tab[0][0], )
                                    elif c == 3 and diagonal[c-1] == 0:
                                        res = res + (tab[2][2], )
                                elif n in diagonal and d == 2:
                                    if c == 1 and diagonal[c-1] == 0:
                                        res = res + (tab[2][0], )
                                    elif c == 3 and diagonal[c-1] == 0:
                                        res = res + (tab[0][2], )    
                                elif n in diagonal and c == 2 and \
                                     diagonal[c-1] == 0:
                                    res = res + (tab[1][1], )                
                
                for d in (1, 2):
                    diagonal = obter_diagonal(tabuleiro, d)
                    if (0-n) not in diagonal and (0-n) not in tabuleiro[l]:
                        if n in diagonal and d == 1:
                            if l == 0 and diagonal[l] == 0:
                                res = res + (tab[0][0], )
                            elif l == 2 and diagonal[l] == 0:
                                res = res + (tab[2][2], )
                        elif n in diagonal and d == 2:
                            if l == 0 and diagonal[2] == 0:
                                res = res + (tab[0][2], )
                            elif l == 2 and diagonal[0] == 0:
                                res = res + (tab[2][0], )    
                        elif n in diagonal and l == 1 and diagonal[l] == 0:
                            res = res + (tab[1][1], )
                        
        return res
                    
    else:
        raise ValueError('bifurcacao: um dos argumentos e invalido')
                         
            
def bloqueio_bifurcacao(tabuleiro, n):
    '''
    tabuleiro x inteiro --> tuplo
    recebe um tabuleiro e devolve um tuplo com a posicao de intersecao da 
    bifurcacao do adversario se so existir uma, senao retorna o tuplo com as 
    posicoes possiveis para fazer um dois em linha e obrigar o jogador oposto a
    defender e tal que esta defesa nao crie uma bifurcacao para o oponente
    '''
    if eh_tabuleiro(tabuleiro) == True and n in (-1, 1):
        tab = ((1,2,3),(4,5,6),(7,8,9))
        res = ()
        if len(bifurcacao(tabuleiro, 0-n)) == 1 or \
           len(bifurcacao(tabuleiro, 0-n)) == 0:
            pos_bifurcacao = bifurcacao(tabuleiro, 0-n)
            res = res + pos_bifurcacao
        
        else:
            for l in (1, 2, 3):
                linha = obter_linha(tabuleiro, l)
                coluna = obter_coluna(tabuleiro, l)
                if linha == (n, 0, 0) or linha == (0, n, 0) or \
                   linha == (0, 0, n):
                    c = [0, 1, 2]
                    for i in (0, 1, 2):
                        if linha[i] == n:
                            del(c[i])
                    for i in range(len(c)):
                        if tab[l-1][c[i]] not in bifurcacao(tabuleiro, 0-n):
                            c1 = c.copy()
                            del(c1[i])
                            col = c1[0]
                            res = res + (tab[l-1][col], )
                            
                if coluna == (n, 0, 0) or coluna == (0, n, 0) or \
                   coluna == (0, 0, n):
                    l1 = [0, 1, 2]
                    for i in (0, 1, 2):
                        if coluna[i] == n:
                            del(l1[i])
                    for i in range(len(l1)):
                        if tab[l1[i]][l-1] not in bifurcacao(tabuleiro, 0-n):
                            l2 = l1.copy()
                            del(l2[i])
                            lin = l2[0]
                            res = res + (tab[lin][l-1], )
                            
            for d in (1, 2):
                diagonal = obter_diagonal(tabuleiro, d)
                tab_pos_diag1 = (1, 5, 9)
                tab_pos_diag2 = (7, 5, 3)
                if diagonal == (n, 0, 0) or diagonal == (0, n, 0) or \
                   diagonal == (0, 0, n):
                    d1 = [0, 1, 2]
                    for i in (0, 1, 2):
                        if diagonal[i] == n:
                            del(d1[i])
                            
                    for i in range(len(d1)):
                        if d == 1:
                            if tab_pos_diag1[d1[i]] not in\
                               bifurcacao(tabuleiro, 0-n):
                                d2 = d1.copy()
                                del(d2[i])
                                diag = d2[0]
                                if diag == 0 and d == 1:
                                    res = res + (tab[0][0], )
                                    
                                elif diag == 2 and d == 1:
                                    res = res + (tab[2][2], )
                                    
                                elif diag == 0 and d == 2:
                                    res = res + (tab[2][0], )
                                    
                                elif diag == 2 and d == 2:
                                    res = res + (tab[0][2], )
                                    
                                elif diag == 1:
                                    res = res + (tab[1][1], )
                                    
                        if d == 2:
                            if tab_pos_diag2[i] not in\
                               bifurcacao(tabuleiro, 0-n):
                                d2 = d1.copy()
                                del(d2[i])
                                diag = d2[0]
                                if diag == 0 and d == 1:
                                    res = res + (tab[0][0], )
                                    
                                elif diag == 2 and d == 1:
                                    res = res + (tab[2][2], )
                                    
                                elif diag == 0 and d == 2:
                                    res = res + (tab[2][0], )
                                    
                                elif diag == 2 and d == 2:
                                    res = res + (tab[0][2], )
                                    
                                elif diag == 1:
                                    res = res + (tab[1][1], )                        
                    
        return res 
        
    else:
        raise  ValueError('bloqueio_bifurcacao: um dos argumentos e invalido')  