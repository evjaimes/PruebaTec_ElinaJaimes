# Elina Jaimes
# Universidad de los Andes

def rangos(m, ranks):
    return None


r = input(
    'Ingrese las parejas de rangos. Escriba los rangos de la siguiente forma. Ej: 1 2 5 6. Sea (1,2) un rango, (5,6) otro \n')

# Limpieza de entrada
limpio = r.split((' '))
for i in range(len(limpio)):
    limpio[i] = int(limpio[i])

next = max(limpio)
rta = rangos(next, limpio)
print('Los nuevos rangos son: {}'.format(rta))
