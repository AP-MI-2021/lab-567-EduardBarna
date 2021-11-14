from Domain.vanzare2 import getPret, getGen
from Logic.CRUD import adauga_vanzare, getById
from Logic.functionalitati import aplica_discount, silver_discount, gold_discount, schimba_gen, pret_min_per_gen, \
    ordonare_vanzari, titluri_distincte_fiecare_gen
from Domain.vanzare2 import getId


def test_silver_discount():
    assert silver_discount(50) == 47.5
    assert silver_discount(100) == 95
    assert silver_discount(20) == 19

def test_gold_discount():
    assert gold_discount(100) == 90
    assert gold_discount(400) == 360
    assert gold_discount(187.68) == 168.912


def test_aplica_discount():
    lista = []
    lista = adauga_vanzare("1", "Ion", "Drama", 20, "silver", lista)
    lista = adauga_vanzare("2", "Morometii", "Drama", 30, "none", lista)
    lista = adauga_vanzare("3", "Dama de pica", "Teatru", 45, "gold", lista)
    lista = adauga_vanzare("4", "Procesul", "Filosofie", 54, "silver", lista)

    lista = aplica_discount(lista)
    assert getPret(getById("1", lista)) == 19
    assert getPret(getById("2", lista)) == 30
    assert getPret(getById("3", lista)) == 40.5
    assert getPret(getById("4", lista)) == 51.3


def test_schimba_gen():
    lista = []
    lista = adauga_vanzare("1", "Ion", "Drama", 20, "silver", lista)
    lista = adauga_vanzare("2", "Morometii", "Drama", 30, "none", lista)
    lista = adauga_vanzare("3", "Dama de pica", "Teatru", 45, "gold", lista)
    lista = adauga_vanzare("4", "Procesul", "Filosofie", 54, "silver", lista)

    lista = schimba_gen("Dama de pica", "Comedie", lista)
    lista = schimba_gen("Procesul", "Drama", lista)
    assert getGen(getById("3", lista)) == "Comedie"
    assert getGen(getById("1", lista)) == "Drama"
    assert getGen(getById("4", lista)) == "Drama"

def test_pret_min_per_gen():
    lista = []
    lista = adauga_vanzare("1", "Ion", "Drama", 20, "silver", lista)
    lista = adauga_vanzare("2", "Morometii", "Drama", 30, "none", lista)
    lista = adauga_vanzare("3", "Dama de pica", "Teatru", 45, "gold", lista)
    lista = adauga_vanzare("4", "Procesul", "Filosofie", 54, "silver", lista)
    lista = adauga_vanzare("5", "Scripcarul", "Teatru", 42, "none", lista)


    assert pret_min_per_gen("Drama", lista) == 20
    assert pret_min_per_gen("Teatru", lista) == 42
    assert pret_min_per_gen("Copii", lista) == None

def test_ordonare_vanzari():
    lista = []
    lista = adauga_vanzare("1", "Ion", "Drama", 98, "silver", lista)
    lista = adauga_vanzare("2", "Morometii", "Drama", 30, "none", lista)
    lista = adauga_vanzare("3", "Dama de pica", "Teatru", 498, "gold", lista)
    lista = adauga_vanzare("4", "Procesul", "Filosofie", 54, "silver", lista)

    lista_sortata = ordonare_vanzari(lista)
    assert getId(lista_sortata[0]) == '2'
    assert getId(lista_sortata[1]) == '4'
    assert getId(lista_sortata[2]) == '1'
    assert getId(lista_sortata[3]) == '3'

def test_titluri_distincte_fiecare_gen():
    lista = []
    lista = adauga_vanzare("1", "Ion", "Drama", 20, "silver", lista)
    lista = adauga_vanzare("2", "Morometii", "Drama", 30, "none", lista)
    lista = adauga_vanzare("3", "Dama de pica", "Teatru", 45, "gold", lista)
    lista = adauga_vanzare("4", "Procesul", "Filosofie", 54, "silver", lista)

    assert titluri_distincte_fiecare_gen("Drama", lista) == 2
    assert titluri_distincte_fiecare_gen("Teatru", lista) == 1
    assert titluri_distincte_fiecare_gen("Comedie", lista) == 0




def test_discount():
    test_aplica_discount()
    test_silver_discount()
    test_gold_discount()


