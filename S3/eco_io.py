# eco_io.py
# Pide tres números y muestra su suma, media y el mayor.

try:
    n1 = float(input("Introduce el primer número: "))
    n2 = float(input("Introduce el segundo número: "))
    n3 = float(input("Introduce el tercer número: "))

    suma = n1 + n2 + n3
    media = suma / 3
    mayor = max(n1, n2, n3)

    print(f"\nSuma: {suma}")
    print(f"Media: {media}")
    print(f"Mayor: {mayor}")

except ValueError:
    print(" Error: Debes introducir solo números.")
