from Teste.TestFunctionalitati import test_discount, test_schimba_gen, test_pret_min_per_gen, test_ordonare_vanzari, \
    test_titluri_distincte_fiecare_gen
from Teste.testCRUD import test_adauga_vanzare, test_sterge_vanzare, test_modifica_vanzare
from Teste.testDomain import test_creaza_vanzare


def test_all():
    test_creaza_vanzare()
    test_adauga_vanzare()
    test_sterge_vanzare()
    test_modifica_vanzare()
    test_discount()
    test_schimba_gen()
    test_pret_min_per_gen()
    test_ordonare_vanzari()
    test_titluri_distincte_fiecare_gen()