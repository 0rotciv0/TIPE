from PIL import Image

img = Image.open("terre.jpg")

def afficher(img):
    img.show()

def pixels(img):
    largeur, hauteur = img.size
    for i in range(hauteur):
        for j in range(largeur):
            pixel = img.getpixel((i,j))
            #print(pixel)
    


def sans_k_bits(img, k :int):
    largeur, hauteur = img.size
    new = Image.new("RGB", (largeur,hauteur), "white")
    for i in range(hauteur):
        for j in range(largeur):
            pixel = img.getpixel((i,j))
            pixel_bin = tuple( map(lambda x : format(x,'08b'), list(pixel)))
            
            #print(tuple(pixel_bin))

            modif_pixel_bin = tuple( map(lambda s : s[:8-k] + ("0"*k), pixel_bin))
            #print(modif_pixel_bin)

            final_en_dec = tuple(map(lambda x : int(x,2), modif_pixel_bin))
            print(final_en_dec)
            new.putpixel((i,j), final_en_dec)
    afficher(new)

pixels(img)
sans_k_bits(img,8)

#https://chatgpt.com/share/674f1e08-9dbc-8009-b563-3a8f8d771dbb