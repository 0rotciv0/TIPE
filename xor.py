def xor(chaine : str, cle: str):
    n = len(chaine)
    assert(n <= len(cle))
    result = ""

    for i in range(n):
        result += str(int(chaine[i])^int(cle[i]))

    return result


def chiffrement(chaine : str, cle : str):
    n = len(cle)
    result = ""
    for i in range(0, len(chaine), n):
        bloc = chaine[i:i+n]
        
        result += xor(bloc, cle)

    return result