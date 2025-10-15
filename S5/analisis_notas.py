# ------------------------------------------------------------
# Programa: analisis_notas.py
# Descripción:
# Pide al usuario una lista de calificaciones separadas por comas,
# valida los datos, calcula estadísticas básicas y muestra un resumen.
# ------------------------------------------------------------

from statistics import mean, multimode  # Para calcular media y moda(n que mas se repite)

try:
    # Pedir lista de notas al usuario
    entrada = input("Introduce las notas separadas por comas (ejemplo: 6.5, 8, 5, 4, 9, 10, 7, 3): ")

    # Separar las notas y convertirlas a números (float)
    notas = [float(n.strip()) for n in entrada.split(",")] # Elimina espacios en blanco y divide la cadena donde haya comas

    # Calcular estadísticas básicas
    total_notas = len(notas)    # Devuelve el numero de elementos de notas
    media = round(mean(notas), 2)    # Redondear a 2 decimales y hacer media
    nota_minima = min(notas)    # Devuelve la nota mas baja
    nota_maxima = max(notas)    #Devuelve la nota mas alta

    # Calcular porcentajes
    aprobados = sum(1 for n in notas if n >= 5)
    sobresalientes = sum(1 for n in notas if n >= 9)
    porcentaje_aprobados = round((aprobados / total_notas) * 100, 2)
    porcentaje_sobresalientes = round((sobresalientes / total_notas) * 100, 2)

    # Calcular moda (nota más repetida)
    moda = multimode(notas)  # Devuelve lista (puede haber varias modas)

    # Evaluación del nivel según la media
    if media >= 8:
        nivel = "Nivel excelente"
    elif 5 <= media < 8:
        nivel = "Nivel medio"
    else:
        nivel = "Necesita refuerzo"

    # Mostrar resultados
    print("\n----- RESUMEN ESTADÍSTICO -----")
    print(f"Número total de notas: {total_notas}")
    print(f"Media: {media}")
    print(f"Nota mínima: {nota_minima}")
    print(f"Nota máxima: {nota_maxima}")
    print(f"Porcentaje de aprobados: {porcentaje_aprobados}%")
    print(f"Porcentaje de sobresalientes: {porcentaje_sobresalientes}%")
    print(f"Nota(s) más repetida(s): {', '.join(map(str, moda))}")
    print(f"Evaluación final: {nivel}")

# Manejo de errores si el usuario introduce algo no numérico
except ValueError:
    print("Error: Asegúrate de introducir solo números separados por comas.")
