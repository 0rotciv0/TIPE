
# Conversion de caractère vers code ASCII en binaire
def char_to_bin(c : str):
    assert(len(c) == 1)
    return bin(ord(c))

# Conversion de chaine de caractères vers tableau contenant 
# les codes ASCII de chaque lettre en bianire
def string_to_bin(s : str): 
    t = []
    for carac in s :
        t.append(char_to_bin(carac))
    return t


# Conversion de binaire vers caractère ASCII
def bin_to_char(b :str):
    return chr(int(b[2:], 2))

# Conversion de tableau de binaire vers chaîne de caractères ASCII
def bin_to_string(t : list):
    chaine = ""
    for nb in t :
        chaine += bin_to_char(nb)
    return chaine 