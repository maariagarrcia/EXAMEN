import random


def minion_game(string):
    palabra_adivinar=string
    
lista = []

def separar_caracteres(string):
    for i in string:
        lista.append(i)
    print(lista)
            
separar_caracteres("hola")

def mezclar_lista(string):
    for letras in lista:
        mezcla=random.sample(lista,len(string))
        print(mezcla)

    
mezclar_lista(lista)