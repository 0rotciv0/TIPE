from carac import *
from decodage import decodage
from image import ouvrir, remplacer_k_bits_upgrade
from carac import string_to_bin_string
from fichier_txt import texte_from_txt
import time

def stegano (image : "str", k : int, chemin : str, caractere_fin : str, xor: str, hamming : bool) :  
    remplacer_k_bits_upgrade(ouvrir(image), k, texte_from_txt(chemin), caractere_fin, xor, hamming) 



# stegano("terre.jpg", 7, "strasbourgeoise.txt", "11110000", "101", True)
stegano("terre.jpg", 7, "les3.txt", "11110000", "101", False)



