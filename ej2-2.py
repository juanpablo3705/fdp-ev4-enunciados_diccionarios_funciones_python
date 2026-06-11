# importar funciones desde funciones-ej2-2.py:
import funcionesej22 as fn2 # fn2 es el seudónimo para llamar el módulo más adelante

# inicializar diccionario vacío:
diccionario_a = {} # acá, no en las funciones, porque este archivo controla los datos del programa

# ciclo menú principal:
while True:

    print("----- MENÚ -----")
    print("1. Agregar alumno")
    print("2. Mostrar alumnos")
    print("3. Ver promedios")
    print("4. Mejor alumno")
    print("5. Cantidad de aprobados")
    print("6. Salir")

    while True:
        try:
            opcion_menu = int(input("Ingrese una opción del menú: "))
            break
        except ValueError:
            print("Error, debe ingresar números del 1 al 6, no letras.")

    match opcion_menu:
        case 1:
            fn2.agregar_alumno(diccionario_a)
        case 2:
            fn2.mostrar_alumnos(diccionario_a)
        case 3:
            fn2.ver_promedios(diccionario_a)
        case 4:
            fn2.mejor_alumno(diccionario_a)
        case 5:
            fn2.cantidad_aprobados(diccionario_a)
        case 6:
            print("Saliendo...")
            break
        case _:
            print("Error, debe seleccionar una opción del 1 al 6.")