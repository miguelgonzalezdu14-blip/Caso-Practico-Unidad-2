# EJERCICIO 2: GESTIÓN DE USUARIOS
import json
import pickle

# 2.1 Registro de usuarios con JSON
usuarios = {}
print("--- REGISTRO DE USUARIOS ---")

while True:
    usr = input("Ingrese nombre de usuario (o 'SALIR' para terminar): ").strip()
    if usr.upper() == "SALIR":
        break
    pwd = input("Ingrese contraseña: ").strip()
    usuarios[usr] = pwd

with open('usuarios.json', 'w', encoding='utf-8') as f:
    json.dump(usuarios, f, indent=4)

# 2.2 Visualización de usuarios registrados
nombres_usuarios = [u for u in usuarios.keys()]
print("\nUsuarios registrados:")
for n in nombres_usuarios:
    print(f"- {n}")

# 2.3 Inicio de sesión con límite de intentos y conversión explícita
max_intentos = 3
print("\n--- INICIO DE SESIÓN ---")

for intento in range(1, max_intentos + 1):
    u_ingresado = input("Usuario: ").strip()
    p_ingresado = input("Contraseña: ").strip()

    pwd_correcta = usuarios.get(u_ingresado)

    if pwd_correcta is not None and pwd_correcta == p_ingresado:
        print(f"\n¡Bienvenido al sistema, {u_ingresado}!")
        break
    else:
        restantes = int(max_intentos - intento)  # Conversión explícita
        if restantes > 0:
            print(f"Credenciales incorrectas. Te quedan {restantes} intento(s).\n")
        elif restantes == 0:
            print("Ha superado el número máximo de intentos permitidos.")
        else:
            print("Acceso denegado.")

# 2.4 Almacenamiento en Fichero Binario (.dat)
with open('usuarios.dat', 'wb') as f_bin:
    pickle.dump(usuarios, f_bin)
print("\nDatos guardados correctamente en formato binario (usuarios.dat).")