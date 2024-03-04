import random

listaCachipun = ["piedra", "papel", "tijeras"]

playerChoice = input("Juega tu opcion (piedra, papel o tijeras): ")
cpuChoice = random.choice(listaCachipun)

if(playerChoice == cpuChoice):

    message = "Han empatado"

elif(playerChoice == "piedra"):

    if(cpuChoice == "papel"):
        message = "Perdiste!!"
    else:
        message = "Ganaste!!"

elif(playerChoice == "papel"):

    if(cpuChoice == "tijeras"):
        message = "Perdiste!!"
    else:
        message = "Ganaste!!"

elif(playerChoice == "tijeras"):

    if(cpuChoice == "piedra"):
        message = "Perdiste!!"
    else:
        message = "Ganaste!!"

else:
    message = "Argumento inválido: Debe ser piedra, papel o tijera"

print(f"Tu jugaste {playerChoice}")
print(f"Computador jugo {cpuChoice}")
print(message)