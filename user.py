from system import cargar_datos, guardar_datos

ARCHIVO_USUARIOS = "data/usuarios.json"

def registrar_usuario():
    usuarios = cargar_datos(ARCHIVO_USUARIOS)

    nombre = input("Nombre: ").lower()
    try:
        edad = int(input("Edad: "))
    except ValueError:
        print("Edad inválida")
        return

    usuario = {
        "nombre": nombre,
        "edad": edad
    }

    usuarios.append(usuario)
    guardar_datos(ARCHIVO_USUARIOS, usuarios)
    print("Usuario registrado correctamente")

def listar_usuarios():
    usuarios = cargar_datos(ARCHIVO_USUARIOS)

    if not usuarios:
        print("No hay usuarios registrados")
        return

    print("\n--- USUARIOS ---")
    for u in usuarios:
        print(f"Nombre: {u['nombre']} | Edad: {u['edad']}")
