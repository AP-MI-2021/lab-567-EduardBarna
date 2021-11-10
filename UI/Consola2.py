from Logic.CRUD import adauga_vanzare, sterge_vanzare, modifica_vanzare
from Logic.functionalitati import aplica_discount, schimba_gen, pret_min_per_gen
from Domain.vanzare2 import ToString


def afisare_all(lista):
    for vanzare in lista:
        print(ToString(vanzare))

def printMeniu():
    print("h.Help")
    print("x.Exit")

def help_menu():
    print("Adauga , id, titlu , gen , pret , tip reducere ----> adaugare vanzare")
    print("Sterge, id ---->sterge o vanzare")
    print("Modifica, id , titlu , gen , pret , tip reducere ----> modifica vanzare")
    print("Discount ----> aplica discount")
    print("Gen, titlu, gen_nou ---> schimba genul unui titlu")
    print("Pret, gen ----> pretul minim")
    print("Afisare")
    print("Break")

def menu2():
    lista = []
    while True:
        printMeniu()
        optiune = input("Introduceti seria de actiuni dorite separate prin ';' cu argumentele separate prin virgula."
                        "Introduceti x pentru iesire. "
                        "Introduceti 'h' pentru ajutor ")
        if optiune == 'h':
            help_menu()
        if optiune == 'x':
            break
        else:
            comenzi = optiune.split(';')
            for c in comenzi:
                actiuni = c.split(',')
                if actiuni[0] == 'Adauga':
                    try:
                        lista = adauga_vanzare(actiuni[1], actiuni[2], actiuni[3], int(actiuni[4]), actiuni[5], lista)
                    except ValueError as ve:
                        print("Eroare: {}".format(ve))
                elif actiuni[0] == 'Sterge':
                    try:
                        lista = sterge_vanzare((actiuni[1]), lista)
                    except ValueError as ve:
                        print("Eroare: {}".format(ve))
                elif actiuni[0] == 'Modifica':
                    try:
                        lista = modifica_vanzare(actiuni[1], actiuni[2], actiuni[3], int(actiuni[4]), actiuni[5], lista)
                    except ValueError as ve:
                        print("Eroare: {}".format(ve))
                elif actiuni[0] == 'Discount':
                    try:
                        lista = aplica_discount(lista)
                    except ValueError as ve:
                        print("Eroare: {}".format(ve))
                elif actiuni[0] == 'Gen':
                    try:
                        lista = schimba_gen(actiuni[1], actiuni [2], lista)
                    except ValueError as ve:
                        print("Eroare: {}".format(ve))
                elif actiuni[0] == 'Pret':
                    try:
                        print(pret_min_per_gen(actiuni[1], lista))
                    except ValueError as ve:
                        print("Eroare: {}".format(ve))
                elif actiuni[0] == "Afisare":
                    try:
                        afisare_all(lista)
                    except ValueError as ve:
                        print("Eroare: {}".format(ve))
                else:
                    print("Optiune Gresita")




