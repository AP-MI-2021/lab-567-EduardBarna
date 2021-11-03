from Domain.vanzare2 import ToString
from Logic.CRUD import adauga_vanzare, sterge_vanzare, modifica_vanzare
from Logic.functionalitati import aplica_discount, schimba_gen, pret_min_per_gen


def printMenu():
    print("1.Adauga vanzare")
    print("2.Sterge vanzare")
    print("3.Modifica vanzare")
    print("4.Aplica discount  de 5% pentru toate reducerile silver și 10% pentru toate reducerile gold.")
    print("5.Schimba genul unei carti cu titlul dat")
    print("6.Afiseaza pretul minim pentru un anume gen")
    print("a.Afiseaza toate vanzarile")
    print("x.Exit")

def ui_adauga_vanzare(lista):
    id = input("Introduceti id-ul: ")
    titlu = input("Introduceti titlul: ")
    gen = input("Introduceti genul: ")
    pret = float(input("Introduceti pretul: "))
    tip_reducere = input("Introduceti tipul de reducere: ")
    return adauga_vanzare(id, titlu, gen, pret, tip_reducere, lista)

def ui_sterge_vanzare(lista):
    id = input("Introduceti id-ul vanzarii ce doriti sa fie sters: ")
    print("Vanzarea a fost stearsa cu succes!")
    return sterge_vanzare(id, lista)

def ui_modifica_vanzare(lista):
    id = input("Introduceti id-ul vanzarii ce doriti sa se modifice: ")
    titlu = input("Introduceti  noul titlu: ")
    gen = input("Introduceti  noul gen: ")
    pret = float(input("Introduceti noul pret: "))
    tip_reducere = input("Introduceti noul tip de reducere: ")
    return modifica_vanzare(id, titlu, gen, pret,tip_reducere, lista)


def ui_afisare_vanzari(lista):
    for vanzare in lista:
        print(ToString(vanzare))

def ui_aplica_discount(lista):
   lista = aplica_discount(lista)
   return lista

def ui_schimba_gen(lista):
    titlu = input("introduceti titlul cartii careia doriti sa ii modificati genul: ")
    gen_nou = input("Introduceti noul gen al cartii: ")
    lista = schimba_gen( titlu, gen_nou, lista)
    return lista

def ui_pret_min_per_gen(lista):
    gen = input("Introduceti genul pentru care doriti sa aflati pretul minim: ")
    return pret_min_per_gen(gen, lista)

def runMenu():
    lista = []
    while True:
        printMenu()
        optiune = input("Dati optiunea:")
        if optiune == '1':
            lista = ui_adauga_vanzare(lista)
        elif optiune == '2':
            lista = ui_sterge_vanzare(lista)
        elif optiune == '3':
            lista = ui_modifica_vanzare(lista)
        elif optiune == '4':
            lista = ui_aplica_discount(lista)
        elif optiune == '5':
            lista = ui_schimba_gen(lista)
        elif optiune =='6':
            print("Pretul minim pentru genul dat este:" + str(ui_pret_min_per_gen(lista)))
        elif optiune == 'a':
            ui_afisare_vanzari(lista)
        elif optiune == 'x':
            break
        else:
            print("Optiune introdusa nu este valida, va rugam reincercati")
