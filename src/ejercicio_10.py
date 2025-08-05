suma = 0
palabra = input("Ingresa una palabra (fin para parar): ")

while palabra != "fin":
    suma += 1
    palabra = input("Ingresa otra palabra (fin para parar): ")

print("La cantidad total de palabras ingresadas es:", suma)
