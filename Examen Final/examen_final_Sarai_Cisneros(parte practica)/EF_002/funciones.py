import random

def gen_lista(num):
    lista = []

    for n in range(num):
        lista.append(random.randint(1, 50))
    print(lista)
    return lista

def no_repet (lista):
    no_repet = list(set(lista))
    print("Sin números repetidos:", no_repet)
    return no_repet

def ordenado(lista):
    ascend = sorted(lista)
    descend = sorted(lista, reverse=True)
    print("Descendente:", descend)
    print("Ascendente:", ascend)
    return descend, ascend