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
    print (lista_numero)
    print (lista_naipe)

    anterior=False
    anteriores=False

    if posicao==0:
        return [] 
    else:
        if lista_naipe[posicao]==lista_naipe[posicao-1] or lista_numero[posicao]==lista_numero[posicao-1]:
            anterior=True
        if (posicao-3)>=0 and (lista_naipe[posicao]==lista_naipe[posicao-3] or lista_numero[posicao]==lista_numero[posicao-3]):
            anteriores=True
            print (lista_naipe [posicao-3], lista_naipe [posicao], lista_numero[posicao], lista_numero[posicao-1], anterior, anteriores)
        if anterior==True and anteriores==True:
            return [1,3]
        elif anterior==True and anteriores==False:
            return [1]
        elif anterior==False and anteriores==True:
            return [3]
        else:
            return []  


print (lista_movimentos_possiveis(['6♥', 'J♥', '9♣', '9♥'], 3))