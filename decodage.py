from PIL import Image
from hamming import decodage_chaine
from xor import chiffrement



def extraction(chemin : str, k : int):
    assert( 0 <= k <= 8)
    im = Image.open(chemin)

    x,y = im.size

    chaine = ""

    for j in range(y):
        for i in range(x):
            pixel = im.getpixel((i,j))
            r,g,b = format(pixel[0], "08b"), format(pixel[1], "08b"), format(pixel[2], "08b")
            #print(f"Composantes du pixel {i,j} : {r[8-k:],g[8-k:],b[8-k:]}")
            chaine += r[8-k:]
            
            chaine += g[8-k:]
            chaine += b[8-k:]



    return chaine


def convertir(chaine : str, caractere_fin : int):
    result = ""
    for i in range(0, len(chaine), 8):
        bloc = chaine[i:i+8]
        if bloc == str(caractere_fin) :
            #print("caractere d'arret trouve !")
            return result
        else : 
            #print(f"bloc n°{i} : {bloc}")
            #print(f"{bloc} -> {chr(int(bloc,2))}")


            # try :
            #     result += chr(int(bloc,2))
            # except UnicodeEncodeError as e :
            #     print("Erreur")

            x = int(bloc,2)
            if x < 128 : 
                result += chr(x)
    
    return result #on est arrivé au bout de la chaine sans avoir rencontré le caractère de fin
        


def decodage(chemin : str, k : int, caractere_fin, hamming : bool, xor :str):
    chaine = extraction(chemin,k)
    #print(f"chaine extraite : {chaine}")

    if hamming : 
        chaine = decodage_chaine(chaine)

    if xor != "" : 
        chaine = chiffrement(chaine, xor)

    print()
    print()
    print()
    print()
    print()
    print()

        
    print(convertir(chaine, caractere_fin))


# decodage("C:/Github/TIPE/tests/s_7_t_101.png", 7, 11110000, True, "101")
# decodage("C:/Github/TIPE/tests/les3_7_t_t.png", 7, 11110000, True, "101")
