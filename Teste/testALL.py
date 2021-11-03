from Teste.TestFunctionalitati import test_discount, test_schimba_gen
from Teste.testCRUD import test_adauga_vanzare, test_sterge_vanzare, test_modifica_vanzare
from Teste.testDomain import test_creaza_vanzare


def test_all():
    test_creaza_vanzare()
    test_adauga_vanzare()
    test_sterge_vanzare()
    test_modifica_vanzare()
    test_discount()
    test_schimba_gen()