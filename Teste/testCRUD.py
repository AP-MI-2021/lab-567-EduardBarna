from Logic.CRUD import adauga_vanzare, getById, sterge_vanzare, modifica_vanzare
from Domain.vanzare2 import getId, getTitlu, getPret, getGen


def test_adauga_vanzare():
    lista = []
    undo_list = []
    redo_list = []

    lista = adauga_vanzare("1", "Ion", "Drama", 20, "silver", lista, undo_list, redo_list)
    lista = adauga_vanzare("2", "Morometii", "Drama", 30, "gold", lista, undo_list, redo_list)
    lista = adauga_vanzare("3", "Dama de pica", "Teatru", 45, "gold", lista, undo_list, redo_list)

    assert len(lista) == 3
    assert getId(getById("1", lista)) == "1"
    assert getTitlu(getById("1", lista)) == "Ion"
    assert getTitlu(getById("2", lista)) == "Morometii"
    assert getPret(getById("3", lista)) == 45

def test_sterge_vanzare():
    lista = []
    undo_list = []
    redo_list = []

    lista = adauga_vanzare("1", "Ion", "Drama", 20, "silver", lista, undo_list, redo_list)
    lista = adauga_vanzare("2", "Morometii", "Drama", 30, "gold", lista, undo_list, redo_list)
    lista = adauga_vanzare("3", "Dama de pica", "Teatru", 45, "gold", lista, undo_list, redo_list)

    lista = sterge_vanzare("2", lista, undo_list, redo_list)

    assert len(lista) == 2
    assert getById("2", lista) is None
    assert getById("1", lista) is not None

def test_modifica_vanzare():
    lista = []
    undo_list = []
    redo_list = []

    lista = adauga_vanzare("1", "Ion", "Drama", 20, "silver", lista, undo_list, redo_list)
    lista = adauga_vanzare("2", "Morometii", "Drama", 30, "gold", lista, undo_list, redo_list)
    lista = adauga_vanzare("3", "Dama de pica", "Teatru", 45, "gold", lista, undo_list, redo_list)

    lista = modifica_vanzare("1", "Procesul", "Filosofie", 45, "none", lista, undo_list, redo_list)

    assert len(lista) == 3
    vanzare_modificata = getById("1", lista)
    assert getId(vanzare_modificata) == "1"
    assert getTitlu(vanzare_modificata) == "Procesul"
    assert getGen(vanzare_modificata) == "Filosofie"
    assert getPret(vanzare_modificata) == 45

    vanzare_nemodificata = getById("2", lista)
    assert getId(vanzare_nemodificata) == "2"
    assert getTitlu(vanzare_nemodificata) == "Morometii"
    assert getGen(vanzare_nemodificata) == "Drama"
    assert getPret(vanzare_nemodificata) == 30



