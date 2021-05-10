# Elina Jaimes
# Universidad de los Andes

def rangos(m, ranks):
    arreglo = [0 for i in range(m+1)]
    for i in range(0, len(ranks), 2):
        a = ranks[i]
        b = ranks[i+1]
        for j in range(a, b+1):
            arreglo[j] = 1

    # Solución
    nuevosRangos = []
    i = 0
    while i < len(arreglo):
        if arreglo[i] == 0:
            pass
        else:
            uno = i
            dos = None
            for j in range(i, len(arreglo)):
                if arreglo[j] == 1:
                    dos = j
                    arreglo[j] = 0
                else:
                    break
            nuevosRangos.append((uno, dos))
        i += 1

    return nuevosRangos


r = input(
    'Ingrese las parejas de rangos. Escriba los rangos de la siguiente forma. Ej: 1 2 5 6. Sea (1,2) un rango, (5,6) otro \n')

# Limpieza de entrada
limpio = r.split((' '))
for i in range(len(limpio)):
    limpio[i] = int(limpio[i])

next = max(limpio)
rta = rangos(next, limpio)
print('Los nuevos rangos son: {}'.format(rta))
