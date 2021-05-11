import random
def cria_baralho():
    letras_e_numeros=['A','2','3','4','5','6','7','8','9','10','J','Q','K']
    naipes=['♣', '♦', '♥', '♠']
    cartas=[]

    for i in letras_e_numeros:
        for e in naipes:
            cartas.append(i+e)    
    return cartas
def extrai_naipe (baralho):
    letras_e_numeros=['A','2','3','4','5','6','7','8','9','10','J','Q','K']
    naipes=['♣', '♦', '♥', '♠']

    for i in letras_e_numeros:
        for e in naipes:
            if e in baralho:
                return e 
def extrai_valor (baralho):
    letras_e_numeros=['A','2','3','4','5','6','7','8','9','10','J','Q','K']
    naipes=['♣', '♦', '♥', '♠']

    for i in letras_e_numeros:
        for e in naipes:
            if i in baralho:
                return i            
def lista_movimentos_possiveis (baralho, posicao):
    lista_naipe=[]
    lista_numero=[]
    for e in baralho:
        naipe=extrai_naipe(e)
        lista_naipe.append(naipe)
        numero=extrai_valor(e)
        lista_numero.append(numero)

    anterior=False
    anteriores=False

    if posicao==0:
        return [] 
    else:
        if lista_naipe[posicao]==lista_naipe[posicao-1] or lista_numero[posicao]==lista_numero[posicao-1]:
            anterior=True
        if (posicao-3)>=0 and (lista_naipe[posicao]==lista_naipe[posicao-3] or lista_numero[posicao]==lista_numero[posicao-3]):
            anteriores=True

        if anterior==True and anteriores==True:
            return [1,3]
        elif anterior==True and anteriores==False:
            return [1]
        elif anterior==False and anteriores==True:
            return [3]
        else:
            return []  
def empilha (baralho, posicao_origem, posicao_destino):
    for i in range (len(baralho)):
        baralho[posicao_destino]=baralho[posicao_origem]
        baralho.pop(posicao_origem)
        break
    return baralho
def possui_movimentos_possiveis (baralho):
    lista_naipe=[]
    lista_numero=[]
    for e in baralho:
        naipe=extrai_naipe(e)
        lista_naipe.append(naipe)
        numero=extrai_valor(e)
        lista_numero.append(numero)

    anterior=False
    anteriores=False

    for e in range (len(baralho)):
        if lista_naipe[e]==lista_naipe[e-1] or lista_numero[e]==lista_numero[e-1]:
            anterior=True
        if (e-3)>=0 and (lista_naipe[e]==lista_naipe[e-3] or lista_numero[e]==lista_numero[e-3]):
            anteriores=True

    if anterior==False and anteriores==False:
        return False
    else:
        return True
def print_baralho(baralho):
    i=0
    j=1
    while i<len(baralho):
        print('{}. {}' .format(j,baralho[i]))
        i+=1
        j+=1
    return ''





def paciencia_acordeao():
    print('-Paciência Acordeão-')
    print('====================')
    #Iniciando jogo
    input('Aperte [ENTER] para que começar a jogar ')
    print('')
    print('')
    deseja_jogar='s'    

    while deseja_jogar=='s':
        baralho=cria_baralho()
        random.shuffle(baralho)    
        while True:
            print('Situação atual do baralho:')
            print('~~~~~~~~~~~~~~~~~~~~~~~~~~~')
            print(print_baralho(baralho))   
            pode_jogar=possui_movimentos_possiveis(baralho)     
            if pode_jogar:
                while True:
                    numero_valido=False
                    while not numero_valido:
                        posicao_origem=int(input('Digite a posição da carta que deseja mover ({}-{}): ' .format('1', len(baralho))))
                        posicao=posicao_origem
                        if (posicao_origem<=0 or posicao_origem>(len(baralho))):
                            return 'Insira um valor válido'
                        else:
                            numero_valido=True
                    referencia=posicao-1
                    movimentos_possiveis=lista_movimentos_possiveis(baralho, referencia)
                    if 1 in movimentos_possiveis or 3 in movimentos_possiveis:
                        if movimentos_possiveis==[1,3]:
                            print('Você possui 2 movimentos possíveis')
                            print('1. {} ' .format(baralho[referencia-1]))
                            print('2. {} ' .format(baralho[referencia-3]))
                            a=True
                            while a:
                                posicao_destino=input(('Sobre qual carta você quer empilhar o {} ? ' .format(baralho[referencia])))
                                if posicao_destino!='1' and posicao_destino!='2':
                                    print('Escolha um número válido (1/2) ')
                                    pass
                                elif posicao_destino=='1':
                                    baralho=empilha(baralho, referencia, referencia-1)
                                    a=False
                                elif posicao_destino=='2':
                                    baralho=empilha(baralho, referencia, referencia-3)
                                    a=False
                        elif movimentos_possiveis==[1]:
                            baralho=empilha(baralho, referencia, referencia-1)
                        elif movimentos_possiveis==[3]:
                            baralho=empilha(baralho, referencia, referencia-3)
                        break
                    else:
                        print ('A carta {} não pode ser movida. Selecione outra carta.' .format(baralho[referencia]))
                        pass
                pass
            else:
                print('Não há mais movimentos possíveis... Você perdeu.') 
                deseja_jogar=input('Deseja jogar novamente? (s/n) ')
                if deseja_jogar!='s':
                    print('Muito obrigado por jogar!')
    return ''

            

print (paciencia_acordeao())