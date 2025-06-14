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
    return x + str(r)

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

    if g != int(s[7]) : 

        i = int(syndrome,2)
        s = s[:i-1] + str(int(s[i-1])^1) + s[i:]


    return s[2] + s[4] + s[5] + s[6]

def decodage_chaine(s:str):
    result = ""
    n = 0
 
    while n < len(s)//8:
        bloc = s[(n*8):(n+1)*8]
        #print(f"bloc n°{n} : {bloc}")
        result += décodage_8_4(bloc)
        n += 1

    result += s[n*8:]
    return result