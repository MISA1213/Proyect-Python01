import json
import os

def cargar_datos(ruta):
    if not os.path.exists(ruta):
        return []

    with open(ruta, "r", encoding="utf-8") as archivo:
        try:
            return json.load(archivo)
        except json.JSONDecodeError:
            return []

def guardar_datos(ruta, datos):
    with open(ruta, "w", encoding="utf-8") as archivo:
        json.dump(datos, archivo, indent=4)

def registrar_usuario(ruta, usuarios):
    try:
        nombre = input("Nombre: ").lower()
        edad = int(input("Edad: "))      
        email = input("Email: ").lower()
    except ValueError:
        print("Edad inválida")
        return
    usuarios = cargar_datos(ruta)
    usuarios.append({"nombre": nombre, "edad": edad, "email": email})
    guardar_datos(ruta, usuarios)   
    

def listar_usuarios(ruta, usuarios):
    if not os.path.exists(ruta):
        print("No hay usuarios registrados")
        return
    else:
        usuarios = cargar_datos(ruta)
        print("\n--- USUARIOS ---")
        for u in usuarios:
            print(f"Nombre: {u['nombre']} | Edad: {u['edad']} | Email: {u['email']}")
        return usuarios