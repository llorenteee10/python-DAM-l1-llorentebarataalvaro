# primo.py
# Determina si un número es primo o no.

try:
    n = int(input("Introduce un número: "))

    if n <= 1:
        print(f"{n} no es primo.")
    else:
        es_primo = True
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                es_primo = False
                break

        if es_primo:
            print(f"{n} es primo.")
        else:
            print(f"{n} no es primo.")

except ValueError:
    print("⚠️ Error: introduce un número entero válido.")
