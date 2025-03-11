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

    print(len(s))
    #print(s)
    print(largeur*hauteur*3*k)
    # assert(len(s) <= largeur*hauteur*3*k)

    for i in range(hauteur):
        for j in range(largeur):
            pixel = img.getpixel((i,j))

            k_bits_fois_trois = s[:k*3] #on prend les k premiers bits à cacher

            s = s[k*3:] #on enleve les k premiers bits

            nouv_pixel = conversion_data_chaine(pixel, k, k_bits_fois_trois)

            new.putpixel((i,j), nouv_pixel)
    afficher(new)


def remplacer_k_bits_upgrade(img, k:int, chaine:str):
    largeur, hauteur = img.size
    new = img.copy()
    s = string_to_bin_string(chaine)

    print(f"nombre de bits à dissimuler : {len(s)}")
    #print(s)
    print(f"nombre de bits disponibles à la dissimulation : {largeur*hauteur*3*k}")
    assert(len(s) <= largeur*hauteur*3*k)
    indice = 0
    while(s!=""):
        i = indice % largeur
        j = indice // largeur 
        #print(i,j)
        pixel = img.getpixel((i,j))

        k_bits_fois_trois = s[:k*3] #on prend les k premiers bits à cacher

        s = s[k*3:] #on enleve les k premiers bits

        nouv_pixel = conversion_data_chaine(pixel, k, k_bits_fois_trois)

        new.putpixel((i,j), nouv_pixel)
        indice += 1

    afficher(new)
# deb = time.time()
# sans_k_bits(img,0)
# fin = time.time()
# print(fin - deb) # 2,8 sec -> 2,1 sec

# sans_k_bits(img,7)


#https://chatgpt.com/share/674f1e08-9dbc-8009-b563-3a8f8d771dbb

"""     Boucle dans sans_k_bits

            # print(pixel)
            # pixel_bin = tuple( map(lambda x : format(x,'08b'), list(pixel)))
            
            # #print(tuple(pixel_bin))

            # modif_pixel_bin = tuple( map(lambda s : s[:8-k] + ("0"*k), pixel_bin))
            # #print(modif_pixel_bin)


            # final_en_dec = tuple(map(lambda x : int(x,2), modif_pixel_bin))
            # #print(final_en_dec)*

"""