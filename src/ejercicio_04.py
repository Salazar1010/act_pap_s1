suma = 0
n =  int(input("Ingresa un numero (0 para parar): "))

while n !=0:
    suma += n
    n = int(input("Ingresa otro numero (0 para parar): "))

print("La suma total de los numeros es: ",suma)