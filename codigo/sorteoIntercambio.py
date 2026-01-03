# -*- coding: utf-8 -*-
"""
Created on Mon Nov  4 15:16:27 2024

@author: Rodrigo
"""

from random import randint

mendonza = ['Letos','Alberto','Rodrigo','Karla','Lucy']
vidal = ['Conrado','Gina','Jesus']
boston = ['Lupis','Mau']
chilangos = ['Carmen','Gabriel','Gaby','Javier']
entregan = [mendonza,vidal,boston,chilangos]
reciben = [lista.copy() for lista in entregan]

def vacio(listaDeListas):
    if all(len(sublista) == 0 for sublista in listaDeListas):
        return True

def rifa(listaEntregan, listaReciben):
    if vacio(listaEntregan) or vacio(listaReciben):
        return True
    else:
        azar = randint(0,len(listaEntregan)-1)
        familia = listaEntregan[azar]
        while (familia == []) == True:
            azar = randint(0,len(listaEntregan)-1)
            familia = listaEntregan[azar]
        persona1 = familia[randint(0,len(familia)-1)]
        azar2 = randint(0,len(listaReciben)-1)
        if azar2 == azar:
            azar2 = randint(0,len(listaReciben)-1)
        familia2 = listaReciben[azar2]
        while (familia2 == []) == True:
            azar2 = randint(0,len(listaReciben)-1)
            familia2 = listaReciben[azar2]
        persona2 = familia2[randint(0,len(familia2)-1)]
        print(f'{persona1} le va a regalar a {persona2}')
        familia.pop(familia.index(persona1))
        familia2.pop(familia2.index(persona2))
    

for i in range(15):
    rifa(entregan, reciben)
