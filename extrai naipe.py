def extrai_naipe (baralho):
    letras_e_numeros=['A','2','3','4','5','6','7','8','9','10','J','Q','K']
    naipes=['♣', '♦', '♥', '♠']

    for i in letras_e_numeros:
        for e in naipes:
            if e in baralho:
                return e 

print(extrai_naipe('A♦'))