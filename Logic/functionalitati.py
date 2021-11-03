
from Domain.vanzare2 import getReducere, getPret, getId, getTitlu, getGen
from Logic.CRUD import  modifica_vanzare


def silver_discount(pret):
    '''
    Returneaza pretul dupa ce s-a aplicat un discount de 5%( silver)
    :param pret: pretul initial
    :return: pretul dupa aplicarea discount-ului
    '''
    discount = pret * 5 / 100
    return pret-discount

def gold_discount(pret):
    '''
    Returneaza pretul dupa ce s-a aplicat un discount de 10% (gold)
    :param pret: pretul initial
    :return: pretul final
    '''
    discount = pret * 10 / 100
    return pret-discount

def aplica_discount(lista):
    '''
    Aplica un discount de 5% (silver) respectiv 10% (gold)
    :param lista:lista initiala
    :return: o noua lista cu discount-urile aplicate elementelor corespunzatoare (silver si gold)
    '''
    for v in lista:
        id = getId(v)
        titlu = getTitlu(v)
        gen = getGen(v)
        pret = getPret(v)
        tip_reducere = getReducere(v)
        if tip_reducere == "silver":
            pret_nou = silver_discount(pret)
            lista = modifica_vanzare(id, titlu, gen, pret_nou, tip_reducere, lista)
        elif tip_reducere == "gold":
            pret_nou = gold_discount(pret)
            lista = modifica_vanzare(id, titlu, gen, pret_nou, tip_reducere, lista)
    return lista



def schimba_gen(titlu_dat, gen_nou, lista):
    '''
    Schimba genul unei carti cu titlul dat
    :param titlu_dat: Titlul cauatat, citit de la tastatura
    :param gen_nou: Noul gen al cartii
    :param lista: lista initiala de vanzari
    :return: lista noua cu elementul corespunzator  avand genul modificat
    '''
    for v in lista:
        id = getId(v)
        titlu = getTitlu(v)
        pret = getPret(v)
        tip_reducere = getReducere(v)
        if getTitlu(v) == titlu_dat:
            lista = modifica_vanzare(id, titlu, gen_nou, pret, tip_reducere, lista)
        else:
            pass
    return lista



