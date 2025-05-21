from PIL import Image 


def extraction(chemin : str, k : int):
    assert( 0 <= k <= 8)
    im = Image.open(chemin)

    y,x = im.size

    chaine = ""

    for i in range(x):
        for j in range(y):
            pixel = im.getpixel((j,i))
            r,g,b = format(pixel[0], "08b"), format(pixel[1], "08b"), format(pixel[2], "08b")
            if i == 0 and (j == 0 or j == 1) :
                print(r[8-k:],g[8-k:],b[8-k:])
            chaine += r[8-k:]
            chaine += g[8-k:]
            chaine += b[8-k:]



    return chaine


def convertir(chaine : str, caractere_fin : int):
    result = ""
    for i in range(0, len(chaine), 8):
        bloc = chaine[i:i+8]
        if bloc == str(caractere_fin) :
            print("caractere d'arret trouvé !")
            return result
        #print(f"{bloc} -> {chr(int(bloc,2))}")
        result += chr(int(bloc,2))
    
    return result #on est arrivé au bout de la chaine sans avoir rencontré le caractère de fin
        

def decodage(chemin : str, k : int, caractere_fin):
    chaine = extraction(chemin,k)
    #print(f"chaine extraite : {chaine}")
    print(convertir(chaine, caractere_fin))