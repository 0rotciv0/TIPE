# stéganographie

#Comment dissimuler la transmission d'un message 
# lors d'un transfert de donnée ?

from PIL import Image

def get_rgb_values(image_path):
    """
    Ouvre une image et retourne un tableau contenant les valeurs RGB de chaque pixel.
    
    :param image_path: chemin de l'image
    :return: une liste de tuples RGB de chaque pixel
    """
    # Ouvre l'image
    with Image.open(image_path) as img:
    
        # Convertit l'image en mode RGB si ce n'est pas déjà le cas
        img = img.convert('RGB')
        
        # Récupère les dimensions de l'image
        width, height = img.size
        
        # Liste pour stocker les valeurs RGB
        rgb_values = []
        
        # Parcourt chaque pixel de l'image et récupère sa valeur RGB
        for y in range(height):
            for x in range(width):
                # Récupère le pixel à la position (x, y)
                r, g, b = img.getpixel((x, y))
                # Ajoute la valeur RGB à la liste
                rgb_values.append((r, g, b))
        
        return rgb_values

# Exemple d'utilisation
image_path = '/home/victor/Documents/Github/TIPE/image.jpg'  # Remplacez par le chemin de votre image
rgb_values = get_rgb_values(image_path)

# Affichage des premières valeurs RGB
print("Premiers pixels RGB : ", rgb_values)