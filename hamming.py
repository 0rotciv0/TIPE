def hamming_7_4(s:str):
    assert(len(s)==4)
    p1 = str(int(s[0])^int(s[1])^int(s[3]))
    p2 = str(int(s[0])^int(s[2])^int(s[3]))
    p3 = str(int(s[1])^int(s[2])^int(s[3]))

    return str(p1 + p2 + s[0] + p3 + s[1] + s[2] + s[3])


def hamming_8_4(s:str):
    assert(len(s)==4)
    x = hamming_7_4(s)
    r = 0
    for i in range(7):
        r= r^int(x[i])
    return str(r)+x


def décodage_8_4(s:str):
    assert(len(s)==8)
    g = 0
    for i in range(7):
        g^= int(s[i])

    #print(g)

    s1 = int(s[0]) ^ int(s[2]) ^ int(s[4]) ^ int(s[6])
    s2 = int(s[1]) ^ int(s[2]) ^ int(s[5]) ^ int(s[6])
    s3 = int(s[3]) ^ int(s[4]) ^ int(s[5]) ^ int(s[6])

    syndrome = str(s3) + str(s2) + str(s1)
    #print(syndrome)

    if g != int(s[7]) : 
        #print("Le nombre d'erreur est impair")

        i = int(syndrome,2)
        #print(f"si l'erreur est unique, elle se trouve en position {i}.")
        s = s[:i-1] + str(int(s[i-1])^1) + s[i:]
        #print(f"La nouvelle chaine est alors {s} ")
        print("Erreur corrigée")
    else : 

        #print("Le nombre d'erreur est pair")

        if syndrome == "000" : 
            print("Il n'y a pas d'erreur.")
        else: 
            #print("Le nombre d'erreur est strictement supérieur à 1.")
            print("Erreur non corrigée")

    return s