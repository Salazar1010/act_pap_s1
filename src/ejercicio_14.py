import random

numero_secreto = random.randint(1, 10)
adivinanza = 0

while adivinanza != numero_secreto:
    adivinanza = int(input("Adivina el número (entre 1 y 10): "))
    
    if adivinanza != numero_secreto:
        print("No adivinaste. Intenta de nuevo.")

print("¡Adivinaste el número! ¡Felicidades!")
