def chiffrement (cle : str, chaine : str): #les entrées sont à fournir en binaire
    nouvChaine = ""
    n = len(cle)
    for i in range(len(chaine)):
        nouvChaine += str( int(chaine[i])^int(cle[i%(n)]) )

    return nouvChaine

print(chiffrement("101","0010101111"))