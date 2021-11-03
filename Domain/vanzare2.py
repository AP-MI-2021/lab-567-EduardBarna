def creaza_vanzare(id, titlu, gen, pret, tip_reducere):
    '''
    Creaza o vanzare

    :param id: string
    :param titlu: string
    :param gen: string
    :param pret: float
    :param tip_reducere: string
    :return: o vanzare
    '''
    return [id, titlu, gen, pret, tip_reducere]

def getId(vanzare):
    return vanzare[0]

def getTitlu(vanzare):
    return vanzare[1]

def getGen(vanzare):
    return vanzare[2]

def getPret(vanzare):
    return vanzare[3]

def getReducere(vanzare):
    return vanzare[4]

def ToString(vanzare):
    return f"ID: {getId(vanzare)}, Titlu: {getTitlu(vanzare)}, " \
           f"Gen: {getGen(vanzare)}, pret: {getPret(vanzare)}, tip reducere: {getReducere(vanzare)}"