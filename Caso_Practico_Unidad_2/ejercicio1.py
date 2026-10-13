# EJERCICIO 1: DON QUIJOTE

# 1.1 Conteo de Sancho vs Dulcinea
with open('datos/quijote.txt', 'r', encoding='utf-8') as f:
    texto = f.read().lower()

sancho = texto.count('sancho')
dulcinea = texto.count('dulcinea')

print(f"Ocurrencias de Sancho: {sancho}")
print(f"Ocurrencias de Dulcinea: {dulcinea}")

if sancho > dulcinea:
    print("Se habla más de Sancho en los primeros capítulos.")
elif dulcinea > sancho:
    print("Se habla más de Dulcinea en los primeros capítulos.")
else:
    print("Se mencionan exactamente la misma cantidad de veces.")

# 1.2 Reescribiendo el Quijote
with open('datos/quijote.txt', 'r', encoding='utf-8') as f_in:
    lineas = f_in.readlines()

lineas_modificadas = [
    linea.replace('Quijote', 'Manolito').replace('quijote', 'manolito')
    for linea in lineas
]

with open('manolito.txt', 'w', encoding='utf-8') as f_out:
    f_out.writelines(lineas_modificadas)

# 1.3 Conteo de palabras (> 100 repeticiones)
import string

contenido = texto
for signo in string.punctuation + '«»¡!¿?':
    contenido = contenido.replace(signo, ' ')

palabras = contenido.split()
frecuencias = {}

for p in palabras:
    frecuencias[p] = frecuencias.get(p, 0) + 1

palabras_top = {k: v for k, v in frecuencias.items() if v > 100}
print("\nPalabras repetidas más de 100 veces:", palabras_top)