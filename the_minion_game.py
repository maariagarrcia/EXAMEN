import random


def minion_game(string):
    palabra_adivinar=string
    
lista = []

def separar_caracteres(string):
    lista=[]
    for i in string:
        lista.append(i)
        print(lista)
    return lista
            
separar_caracteres("hola")

def mezclar_lista(string):


    for letras in lista:
        mezcla=random.sample(lista,len(string))
        print(mezcla)
        StrLista = "".join(mezcla)
        print(StrLista)

        return StrLista


    

mezclar_lista(lista)