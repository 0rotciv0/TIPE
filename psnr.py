from PIL import Image
from math import log10

def eqm (i1 : str, i2 : str):
    image1 = Image.open(i1)
    image2 = Image.open(i2)
    assert(image1.size==image2.size)
    m,n = image1.size

    resultat = 0
    for i in range(m):
        for j in range(n):
            for k in range(3):
                resultat += ( image1.getpixel((i,j))[k] - image2.getpixel((i,j))[k] )**2
    resultat = resultat / (m*n*3)
    # print(resultat)
    return resultat

def psnr(i1 : str, i2 : str):
    x = eqm(i1,i2)
    if x == 0 :
        return f"""Les images "{i1}" et "{i2}" sont parfaitement identiques"""
    return f"""Le rapport PSNR entre les images "{i1}" et "{i2}" vaut {255/x} (= {10*log10(255/x)} dB)"""


print(psnr("terre.jpg", "terre.jpg"))
for i in range(2,9):
    print(psnr("terre.jpg", f"tests/terre_{i}.jpg"))

