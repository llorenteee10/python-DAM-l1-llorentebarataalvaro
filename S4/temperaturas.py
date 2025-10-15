# temperaturas.py
# Convierte temperaturas entre Celsius, Kelvin y Fahrenheit.

print("Conversor de temperaturas")
grados = float(input("Introduce la temperatura en grados Celsius: "))

print("¿A qué unidad quieres convertir?")
print("1. Kelvin")
print("2. Fahrenheit")

opcion = input("Elige una opción (1 o 2): ")

if opcion == "1":
    resultado = grados + 273.15
    print(f"{grados} °C = {resultado} K")
elif opcion == "2":
    resultado = (grados * 9/5) + 32
    print(f"{grados} °C = {resultado} °F")
else:
    print("Opción no válida.")
