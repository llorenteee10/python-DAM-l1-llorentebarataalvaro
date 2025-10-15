# lista_numeros.py
# Pide una lista de números separados por comas y calcula estadísticas.

entrada = input("Introduce números separados por comas: ")

try:
    numeros = [float(n.strip()) for n in entrada.split(",")]
    suma = sum(numeros)
    media = suma / len(numeros)
    maximo = max(numeros)

    # Detección de duplicados
    duplicados = [n for n in set(numeros) if numeros.count(n) > 1]

    print(f"\nSuma: {suma}")
    print(f"Media: {media}")
    print(f"Máximo: {maximo}")
    print(f"Duplicados: {duplicados if duplicados else 'No hay duplicados'}")

except ValueError:
    print("Error: asegúrate de escribir solo números separados por comas.")
