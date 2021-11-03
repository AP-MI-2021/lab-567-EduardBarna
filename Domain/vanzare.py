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
    return{
        'id':id,
        'titlu':titlu,
        'gen':gen,
        'pret':pret,
        'tip_reducere':tip_reducere
    }

def getId(vanzare):
    return vanzare['id']

def getTitlu(vanzare):
    return vanzare['titlu']

def getGen(vanzare):
    return vanzare['gen']

def getPret(vanzare):
    return vanzare['pret']

def getReducere(vanzare):
    return vanzare['tip_reducere']

def ToString(vanzare):
    return f"ID: {getId(vanzare)}, Titlu: {getTitlu(vanzare)}, " \
           f"Gen: {getGen(vanzare)}, pret: {getPret(vanzare)}, tip reducere: {getReducere(vanzare)}"
