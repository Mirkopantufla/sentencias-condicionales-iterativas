import math
# W : corresponde al peso de la persona en Kg.
# H: corresponde a la altura en metros.
# IMC: EL valor del IMC, en [Kg/m2]
inputPesoKg = float(input("Escriba su peso en kg (ej: 81): "))
inputAlturaCm = float(input("Escriba su altura en centimetros (ej: 178): "))

imc = inputPesoKg / math.pow((inputAlturaCm/100), 2)
message = ""

if(imc < 8.5):
    message = "Bajo Peso"
elif(imc >= 18.5 and imc < 25):
    message = "Adecuado"
elif(imc >= 25 and imc < 30):
    message = "Sobrepeso"
elif(imc >= 30 and imc < 35):
    message = "Obesidad Grado I"
elif(imc >= 35 and imc < 40):
    message = "Obesidad Grado II"
elif(imc >= 40):
    message = "Obesidad Grado III"
else:
    message = "Algo ha pasado"

print(f'Su IMC es: {"{:.2f}".format(imc)}')
print(f"La clasificación OMS es {message}")