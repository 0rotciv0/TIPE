def encoder(s : str):
    assert(len(s) == 4)
    p1 = int(s[0])^int(s[1])^int(s[3])
    p2 = int(s[0])^int(s[2])^int(s[3])
    p3 = int(s[1])^int(s[2])^int(s[3])

    return str(p1) + str(p2) + s[0] + str(p3) + s[1] + s[2] + s[3]

