# cadenas.py
# Cuenta vocales, consonantes, mayúsculas y caracteres totales.

texto = input("Introduce una cadena: ")

vocales = "aeiouáéíóúAEIOUÁÉÍÓÚ"
num_vocales = sum(1 for c in texto if c in vocales)
num_consonantes = sum(1 for c in texto if c.isalpha() and c not in vocales)
num_mayusculas = sum(1 for c in texto if c.isupper())
num_caracteres = len(texto)

print(f"\nVocales: {num_vocales}")
print(f"Consonantes: {num_consonantes}")
print(f"Mayúsculas: {num_mayusculas}")
print(f"Número total de caracteres: {num_caracteres}")
