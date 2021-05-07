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


def paciencia_acordeao():
    print('-Paciência Acordeão-')
    print('====================')
    baralho=cria_baralho()
    random.shuffle(baralho)
    pode_jogar=possui_movimentos_possiveis(baralho)

    if pode_jogar==True:
        print('Situação atual do baralho:')
        print('~~~~~~~~~~~~~~~~~~~~~~~~~~~')

        i=1
        while i<53:
            print('{}. {}' .format(i,baralho[i-1]))
            i+=1

        posicao_origem=input('Digite a posicao da carta que deseja mover ({}-{}): ' .format('1', len(baralho)))

        for e in range (len(baralho)):
            if e==posicao_origem:
                naipe_pos_origem=extrai_naipe(e)
                valor_pos_origem=extrai_valor(e)
                print (valor_pos_origem, naipe_pos_origem)
            
        pode_jogar=False

print (paciencia_acordeao())