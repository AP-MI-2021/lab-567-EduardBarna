from Domain.vanzare2 import ToString
from Logic.CRUD import adauga_vanzare, sterge_vanzare, modifica_vanzare
from Logic.functionalitati import aplica_discount, schimba_gen, pret_min_per_gen, ordonare_vanzari, \
    titluri_distincte_fiecare_gen, do_undo, do_redo


def printMenu():
    print("1.Adauga vanzare")
    print("2.Sterge vanzare")
    print("3.Modifica vanzare")
    print("4.Aplica discount  de 5% pentru toate reducerile silver și 10% pentru toate reducerile gold.")
    print("5.Schimba genul unei carti cu titlul dat")
    print("6.Afiseaza pretul minim pentru un anume gen")
    print("7.Ordoneza vanzarile crescator dupa pret")
    print("8.Afisati nr de titluri distincte pentru fiecare gen")
    print("u.Undo")
    print("r.Redo")
    print("a.Afiseaza toate vanzarile")
    print("x.Exit")

def ui_adauga_vanzare(lista, undo_list, redo_list):
    try:
        id = input("Introduceti id-ul: ")
        titlu = input("Introduceti titlul: ")
        gen = input("Introduceti genul: ")
        pret = float(input("Introduceti pretul: "))
        tip_reducere = input("Introduceti tipul de reducere: ")
        return adauga_vanzare(id, titlu, gen, pret, tip_reducere, lista,undo_list, redo_list,)

    except ValueError as ve:
        print("Eroare: {}".format(ve))
        return lista

def ui_sterge_vanzare(lista, undo_list, redo_list):
    try:
        id = input("Introduceti id-ul vanzarii ce doriti sa fie sters: ")
        print("Vanzarea a fost stearsa cu succes!")
        rezultat = sterge_vanzare(id, lista, undo_list, redo_list)
        return rezultat
    except ValueError as ve:
        print("Eroare: {}".format(ve))
        return lista

def ui_modifica_vanzare(lista, undo_list, redo_list):
    try:
        id = input("Introduceti id-ul vanzarii ce doriti sa se modifice: ")
        titlu = input("Introduceti  noul titlu: ")
        gen = input("Introduceti  noul gen: ")
        pret = float(input("Introduceti noul pret: "))
        tip_reducere = input("Introduceti noul tip de reducere: ")
        rezultat = modifica_vanzare(id, titlu, gen, pret,tip_reducere, lista, undo_list, redo_list)
        return rezultat
    except ValueError as ve:
        print("Eroare: {}".format(ve))
        return lista



def ui_afisare_vanzari(lista):
    for vanzare in lista:
        print(ToString(vanzare))

def ui_aplica_discount(lista, undo_list, redo_list):
    try:
        rezultat = aplica_discount(lista, undo_list, redo_list)
        return rezultat
    except ValueError as ve:
        print("Eroare: {}".format(ve))
        return lista


def ui_schimba_gen(lista, undo_list, redo_list):
    try:
        titlu = input("introduceti titlul cartii careia doriti sa ii modificati genul: ")
        gen_nou = input("Introduceti noul gen al cartii: ")
        rezultat = schimba_gen(titlu, gen_nou, lista, undo_list, redo_list)
        return rezultat

    except ValueError as ve:
        print("Eroare: {}".format(ve))
        return lista


def ui_pret_min_per_gen(lista):
    try:
        gen = input("Introduceti genul pentru care doriti sa aflati pretul minim: ")
        rezultat = pret_min_per_gen(gen, lista)
        return rezultat
    except ValueError as ve:
        print("Eroare: {}".format(ve))
        return lista

def ui_ordonare_vanzari(lista):
    return ordonare_vanzari(lista)

def ui_afisare_titluri_per_gen(lista):
    gen = input("Dati genul cartii: ")
    print(f"Numarul de titluri distincte pentru genul {gen}: {titluri_distincte_fiecare_gen(gen, lista)}")




def runMenu():
    lista = []
    undo_list = []
    redo_list = []
    while True:
        printMenu()
        optiune = input("Dati optiunea:")
        if optiune == '1':
            lista = ui_adauga_vanzare(lista, undo_list, redo_list)
        elif optiune == '2':
            lista = ui_sterge_vanzare(lista, undo_list, redo_list)
        elif optiune == '3':
            lista = ui_modifica_vanzare(lista, undo_list, redo_list)
        elif optiune == '4':
            lista = ui_aplica_discount(lista, undo_list, redo_list)
        elif optiune == '5':
            lista = ui_schimba_gen(lista, undo_list, redo_list)
        elif optiune == '6':
            print("Pretul minim pentru genul dat este:" + str(ui_pret_min_per_gen(lista)))
        elif optiune == '7':
            print(ui_ordonare_vanzari(lista))
        elif optiune == '8':
            ui_afisare_titluri_per_gen(lista)
        elif optiune == 'u':
            previous_list = do_undo(undo_list, redo_list, lista)
            if previous_list is not None:
                lista = previous_list
            else:
                print("Nu se poate face undo!")
        elif optiune == 'r':
            previous_list = do_redo(undo_list, redo_list, lista)
            if previous_list is not None:
                lista = previous_list
            else:
                print("Nu se poate face redo!")

        elif optiune == 'a':
            ui_afisare_vanzari(lista)
        elif optiune == 'x':
            break
        else:
            print("Optiune introdusa nu este valida, va rugam reincercati")
