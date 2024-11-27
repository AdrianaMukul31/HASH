def primer_caracter_no_repetido(cadena):
    conteo = {}  
    for char in cadena:
        if char in conteo:
            conteo[char] += 1
        else:
            conteo[char] = 1
    for char in cadena:
        if conteo[char] == 1:
            return char

    return None  

cadena = "aabccdbef"
resultado = primer_caracter_no_repetido(cadena)
print("Primer carácter no repetido:", resultado)
