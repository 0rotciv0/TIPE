from PIL import Image
import random

def ajouter_bruit(chemin, intensite_bruit=0.01):

    img = Image.open(chemin).convert("RGB")
    pixels = img.load()
    largeur, hauteur = img.size

    nombre_pixels = int(largeur * hauteur * intensite_bruit)

    for _ in range(nombre_pixels):
        x = random.randint(0, largeur - 1)
        y = random.randint(0, hauteur - 1)
        r, g, b = pixels[x, y]

        # Choisir une composante aléatoire à modifier
        composante = random.choice([0, 1, 2])
        bruit = random.randint(0, 255)

        if composante == 0:
            pixels[x, y] = (bruit, g, b)
        elif composante == 1:
            pixels[x, y] = (r, bruit, b)
        else:
            pixels[x, y] = (r, g, bruit)

    img.show()
