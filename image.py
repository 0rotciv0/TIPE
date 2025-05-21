from PIL import Image
from carac import string_to_bin_string
import time #pour calculer les durées d'exécution du programme

def ouvrir(s):
    return Image.open(s)

def afficher(img):
    img.show()

def pixels(img):
    largeur, hauteur = img.size
    for i in range(hauteur):
        for j in range(largeur):
            pixel = img.getpixel((i,j))
            #print(pixel)
    
def conversion_data_0 (t : tuple, k : int) : 
    l = list(t)
    for i in range(3) :
        l[i] = format(l[i],'08b')
        l[i] =  l[i][:8-k] + "0"*k
        l[i] = int(l[i], 2)
    return tuple(l)
        
def conversion_data_chaine (t : tuple, k : int, k_bits_fois_trois : str) : 
    l = list(t)
    for i in range(3) :
        l[i] = format(l[i],'08b')
        x = k_bits_fois_trois[i*k:(i+1)*k]
        if x != "" : 
            l[i] =  l[i][:8-k] + x

        #si on a plus rien à cacher, on fait le choix de ne rien modifier
        # --> cela ne crée pas une forntière avec la partie modifiée ?

        l[i] = int(l[i], 2)
    return tuple(l)


def sans_k_bits(img, k :int):
    largeur, hauteur = img.size
    new = Image.new("RGB", (largeur,hauteur), "white")
    for i in range(hauteur):
        for j in range(largeur):
            pixel = img.getpixel((i,j))
            new.putpixel((i,j), conversion_data_0(pixel, k))
    afficher(new)

def remplacer_k_bits(img, k:int, chaine:str):
    largeur, hauteur = img.size
    new = Image.new("RGB", (largeur,hauteur), "white")
    s = string_to_bin_string(chaine)

    #print(len(s))
    #print(s)
    #print(largeur*hauteur*3*k)
    # assert(len(s) <= largeur*hauteur*3*k)

    for i in range(hauteur):
        for j in range(largeur):
            pixel = img.getpixel((i,j))

            k_bits_fois_trois = s[:k*3] #on prend les k premiers bits à cacher

            s = s[k*3:] #on enleve les k premiers bits

            nouv_pixel = conversion_data_chaine(pixel, k, k_bits_fois_trois)

            new.putpixel((i,j), nouv_pixel)
    afficher(new)


def remplacer_k_bits_upgrade(img, k:int, chaine:str, caractere_fin : str):
    largeur, hauteur = img.size
    new = img.copy()
    s = string_to_bin_string(chaine) + str(caractere_fin)
    #print(f"chaine cachée : {s}\n\n\n")

    #print(f"nombre de bits à dissimuler : {len(s)}")
    #print(s)
    #print(f"nombre de bits disponibles à la dissimulation : {largeur*hauteur*3*k}")
    assert(len(s) <= largeur*hauteur*3*k)
    indice = 0

    while(s!=""):
        i = indice % largeur #abscisse
        j = indice // largeur #ordonnée
        #print(i,j)
        pixel = img.getpixel((i,j))
        #print(f"pixel de base en ({i},{j}) : {pixel}")

        k_bits_fois_trois = s[:k*3]#on prend les k premiers bits à cacher
        #print(f"à ajouter : {k_bits_fois_trois}")

        s = s[k*3:] #on enleve les k premiers bits

        nouv_pixel = ["","",""]
        for m in range(3):
            a , b = format(pixel[m], "08b") , k_bits_fois_trois[m*k:(m+1)*k]
            #print(f"en binaire : {a} puis {a[:8-k]}")
            
            if b != "" :
                nouv_pixel[m] = a[:8-k] + b
            else :
                nouv_pixel[m] = a
                
            #print(f"on rajoute {b} ce qui donne {nouv_pixel[m]}")

            nouv_pixel[m] = int(nouv_pixel[m],2)
            #print(f"puis en décimal : {nouv_pixel[m]}")
        #print()
        new.putpixel((i,j), tuple(nouv_pixel))
        indice += 1

    print(f"dernier pixel en ligne {indice // largeur} et colonne {indice % largeur}")
    afficher(new)
    new.save(f"tests/r&j/test_{k}.jpg")

