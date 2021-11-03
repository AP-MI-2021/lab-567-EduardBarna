from Domain.vanzare2 import creaza_vanzare, getId, getTitlu, getGen, getPret, getReducere


def test_creaza_vanzare():
    vanzare = creaza_vanzare("1", "Ion", "Drama", 20, "silver")

    assert getId(vanzare) == "1"
    assert getTitlu(vanzare) == "Ion"
    assert getGen(vanzare) == "Drama"
    assert getPret(vanzare) == 20
    assert getReducere(vanzare) == "silver"