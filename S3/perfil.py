# Programa que pide nombre, fecha de nacimiento (día, mes, año),
# calcula la edad, clasifica por tramo y determina el signo zodiacal.

from datetime import date

def obtener_signo(dia, mes):
    """Devuelve el signo zodiacal segun el dia y el mes de nacimiento"""
    if (mes == 3 and dia >= 21) or (mes == 4 and dia <= 19):
        return "Aries"
    elif (mes == 4 and dia >= 20) or (mes == 5 and dia <= 20):
        return "Tauro"
    elif (mes == 5 and dia >= 21) or (mes == 6 and dia <= 20):
        return "Géminis"
    elif (mes == 6 and dia >= 21) or (mes == 7 and dia <= 22):
        return "Cáncer"
    elif (mes == 7 and dia >= 23) or (mes == 8 and dia <= 22):
        return "Leo"
    elif (mes == 8 and dia >= 23) or (mes == 9 and dia <= 22):
        return "Virgo"
    elif (mes == 9 and dia >= 23) or (mes == 10 and dia <= 22):
        return "Libra"
    elif (mes == 10 and dia >= 23) or (mes == 11 and dia <= 21):
        return "Escorpio"
    elif (mes == 11 and dia >= 22) or (mes == 12 and dia <= 21):
        return "Sagitario"
    elif (mes == 12 and dia >= 22) or (mes == 1 and dia <= 19):
        return "Capricornio"
    elif (mes == 1 and dia >= 20) or (mes == 2 and dia <= 18):
        return "Acuario"
    else:
        return "Piscis"

try:
    # Pedir datos al usuario
    nombre = input("Introduce tu nombre: ")
    dia = int(input("Introduce tu día de nacimiento (1-31): "))
    mes = int(input("Introduce tu mes de nacimiento (1-12): "))
    anio = int(input("Introduce tu año de nacimiento: "))

    # Calcular edad
    anio_actual = date.today().year
    edad = anio_actual - anio

    # Clasificar tramo de edad
    if edad < 18:
        tramo = "Menor de 18 años"
    elif 18 <= edad <= 65:
        tramo = "Entre 18 y 65 años"
    else:
        tramo = "Mayor de 65 años"

    # Obtener signo zodiacal
    signo = obtener_signo(dia, mes)

    # Mostrar resultado
    print(f"\nHola {nombre}, tienes {edad} años, estás en el tramo: {tramo} y tu signo zodiacal es {signo}")

except ValueError:
    print("Error: Debes introducir números válidos para la fecha.")
