from Domain.vanzare2 import creaza_vanzare, getId


def getById(id, lista):
    '''
    Returneaza o vanzare cu id-ul dat
    :param id:id-ul cautat
    :return:vanzarea cu id-ul cautat
    '''
    for v in lista:
        if getId(v) == id:
            return v
    return None

def adauga_vanzare(id, titlu, gen, pret, tip_reducere ,lista, undo_list, redo_list):
    '''
    Adauga o vanzare la o lista ce contine alte vanzari
    :param id: id-ul cartii
    :param titlu: titlul cartii
    :param gen: genul cartii
    :param pret: pretul cartii
    :param tip_reducere: tipul reducerii clientului
    :param lista: lista initiala de vanzari
    :return: lista initiala + vanzarea adaugata
    '''
    if getById(id, lista) is not None:
        raise ValueError("Id-ul exista deja!")
    vanzare = creaza_vanzare(id, titlu, gen, pret, tip_reducere)

    undo_list.append(lista)
    redo_list.clear()
    return lista + [vanzare]

def sterge_vanzare(id, lista, undo_list, redo_list):
    '''
    Sterge o vanzare cu id-ul dat dintr-o lista
    :param id: id-ul dat
    :param lista: lista initiala
    :return: lista fara elementul cu id-ul dat
    '''
    if getById(id, lista) is None:
        raise ValueError("Nu exista o vanzare cu id-ul dat!")

    undo_list.append(lista)
    redo_list.clear()
    return [v for v in lista if getId(v) != id]

def modifica_vanzare(id, titlu, gen, pret, tip_reducere,lista, undo_list, redo_list):
    '''
    Modifica o vanzare cu id-ul dat
    :param id: id-ul cautat
    :param titlu: Noul titlu
    :param gen: noul gen
    :param pret: noul pret
    :param tip_reducere: noul tip de reducere
    :param lista: lista initiala
    :return: noua lista
    '''
    if getById(id, lista) is None:
        raise ValueError("Nu exista o vanzare cu id-ul dat!")

    listaNoua = []
    for v in lista:
        if getId(v) == id:
            vanzare_noua = creaza_vanzare(id, titlu, gen, pret, tip_reducere)
            listaNoua.append(vanzare_noua)
        else:
            listaNoua.append(v)
    undo_list.append(lista)
    redo_list.clear()
    return listaNoua


