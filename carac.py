
# Conversion de caractère vers code ASCII en binaire
def char_to_bin(c : str):
    assert(len(c) == 1)
    return format(ord(c),'08b')

# Conversion de chaine de caractères vers tableau contenant 
# les codes ASCII de chaque lettre en bianire
def string_to_bin(s : str): 
    t = []
    for carac in s :
        t.append(char_to_bin(carac))
    return t

def string_to_bin_string(chaine : str): 
    s = ""
    for carac in chaine :
        s = s + char_to_bin(carac)
    return s

# Conversion de binaire vers caractère ASCII
def bin_to_char(b :str):
    return chr(int(b[2:], 2))

# Conversion de tableau de binaire vers chaîne de caractères ASCII
def bin_to_string(t : list):
    chaine = ""
    for nb in t :
        chaine += bin_to_char(nb)
    return chaine 

def partitionner_4_string(s : str) : 
    l = string_to_bin(s) 
    resultat = []
    for elem in l : 
        resultat.append(elem[:4])
        resultat.append(elem[4:])
    return resultat

# print(char_to_bin("e"))
# print(string_to_bin("test"))
# print(string_to_bin_string("test"))
