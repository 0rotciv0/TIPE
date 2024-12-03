# Caractère à convertir
caractere = 'A'  # Par exemple, le caractère 'A'

utf8_encoded = caractere.encode('utf-8')



def decimal_a_binaire_8_bits(decimal : int) -> str:
    if decimal < 0 or decimal > 255:
        raise ValueError("Le nombre doit être entre 0 et 255 pour être représenté sur 8 bits.")
    
    binaire = bin(decimal)[2:] #on enelve '\b' au début
    
    binaire_8_bits = ''.join(['0' for i in range(8-len(binaire))]) + binaire #on rajoute les 0 nécéssaires pour arriver à un codage 8 bits
    
    return binaire_8_bits

print(utf8_encoded)
for byte in utf8_encoded:
    print(decimal_a_binaire_8_bits(byte))
