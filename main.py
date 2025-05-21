from carac import *
from decodage import decodage
from image import ouvrir, remplacer_k_bits_upgrade
from carac import string_to_bin_string
from hamming import encoder
from fichier_txt import texte_from_txt

def stegano (image : "str", k : int, chemin : str, caractere_fin : str) :  
    remplacer_k_bits_upgrade(ouvrir(image), k, texte_from_txt(chemin), caractere_fin) 


for i in range (1,9):
    print(f"\n\nTest effectué avec k={i} :\n")
    stegano("terre.jpg", i, "romeo_et_juliette.txt", "11110000")
# stegano("meditation.jpg", 6, "strasbourgeoise.txt")

#stegano("terre.jpg", 7, "romeo_et_juliette.txt", "11110000")
# stegano("terre.jpg", 4, "Fahrenheit.txt", "11110000")

#stegano("cafe.jpg", 7, "strasbourgeoise.txt")


