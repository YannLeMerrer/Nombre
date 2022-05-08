import random
number = random.randint(1,101)
attempts = 0
value = "0"
while int(value) != number :
    value = input("Entrez un nombre : ")
    if int(value) > number:
        print("Nombre trop grand")
        
    if int(value) < number:
        print("nombre trop petit")

    attempts += 1
if attempts == 1 :
    print(f"Vous avez gagné, vous avez réussi en {attempts} essai !")

if attempts > 1 :
    print(f"Vous avez gagné, votre nombre d'essais est de : {attempts}")