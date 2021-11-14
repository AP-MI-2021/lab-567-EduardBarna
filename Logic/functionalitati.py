
from Domain.vanzare2 import getReducere, getPret, getId, getTitlu, getGen
from Logic.CRUD import modifica_vanzare


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

def pret_min_per_gen(gen, lista):
    '''
    Returneaza pretul minim pentru un anume gen
    :param gen: genul cartii
    :param lista: lista cu vanzari
    :return:pretul minim pentru un gen dat
    '''
    pret_min = None
    for v in lista:
        if gen == getGen(v):
            pret = getPret(v)
            if pret_min is not None and pret < pret_min:
                pret_min = pret
            elif pret_min is None:
                pret_min = pret
            else:
                pass
    return pret_min


def ordonare_vanzari(lista):
    '''
    Ordoneaza vânzările crescător după preț
    :param lista:lista de vanzari
    :return:lista modificata cu vanzarile ordonate crescator in functie de pret
    '''
    return sorted(lista, key=lambda vanzare: getPret(vanzare))



def titluri_distincte_fiecare_gen(gen, lista):
    '''
    Determina numarul de titluri distincte pentru un anume gen
    :param gen: genul dat
    :param lista: lista de vanzari
    :return: nr de titluri distincte pentru un gen dat
    '''
    nr_titluri = 0
    lst_titluri = []
    for v in lista:
        titlu = getTitlu(v)
        if gen == getGen(v) and titlu not in lst_titluri:
            nr_titluri += 1
            lst_titluri.append(titlu)
    return nr_titluri






