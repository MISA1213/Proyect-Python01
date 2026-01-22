from system import registrar_usuario, listar_usuarios
ARCHIVO_USUARIOS = "data/datos.json"

def menu_principal():
    while True:
        print("\n--- SISTEMA DE GESTIÓN DE USUARIOS ---")
        print("1. Registrar usuario")
        print("2. Listar usuarios")
        print("3. Salir")

        opcion = input("Elegí una opción: ")

        if opcion == "1":
            registrar_usuario(ruta=ARCHIVO_USUARIOS, usuarios=[])
        elif opcion == "2":
            listar_usuarios(ruta=ARCHIVO_USUARIOS, usuarios=[])
        elif opcion == "3":
            print("Saliendo del sistema...")
            break
        else:
            print("Opción inválida")