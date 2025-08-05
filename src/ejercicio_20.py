edad = 0
edad_maxima = None 

while edad != -1:
    edad = int(input("Ingresa una edad (-1 para terminar): "))
    
    if edad != -1:
        if (edad_maxima is None) or (edad > edad_maxima):
            edad_maxima = edad

if edad_maxima is not None:
    print("La edad mayor ingresada es:", edad_maxima)
else:
    print("No se ingresaron edades.")
