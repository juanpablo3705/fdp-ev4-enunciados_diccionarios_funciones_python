# inicializar diccionario vacío:
diccionario_a = {}

# 1 función agregar alumno:
def agregar_alumno(diccionario_a):

    nombre = input("Ingrese el nombre del alumno: ")
    if (nombre == "") or (nombre in diccionario_a):
        print("Error, el nombre no puede estar vacío ni repetirse con uno ya existente.")
        return # usar return en vez de else para mejor orden. vuelve al inicio de def
    
    while True:
        try:
            notas_ingresar = int(input("Ingrese la cantidad de notas a registrar: "))
            if (notas_ingresar > 0):
                print(f"A continuación, registre {notas_ingresar} notas.")
                break
            else:
                print("Error, debe registrar al menos una nota.")
        except ValueError:
            print("Error, el valor debe ser numérico, sin decimales ni letras.")

    while True:
        try:
            lista_notas = []
            for i in range(notas_ingresar):   # usa range porque notas_ingresar no es iterable (es solo 1 numero)
                cada_nota = float(input(f"Ingrese la nota número {i + 1}: "))
                if (cada_nota >= 1) and (cada_nota <= 7):
                    print(f"Nota {i + 1} ingresada con éxito.")
                    lista_notas.append(cada_nota)  # método para agregar nota a una lista
                else:
                    print("Error, la nota debe estar entre 1.0 y 7.0. Intente otra vez.")
                    return  # aborta el ingreso de notas si una de las notas es menor a 1 o mayor a 7
            break
        except ValueError:
            print("Error, las notas deben ser números, no letras.")

    diccionario_a[nombre] = [lista_notas]

# 2 función mostrar alumnos:
def mostrar_alumnos(diccionario_a):
    if len(diccionario_a) == 0:   # diccionario vacío, usar len()
        print("Error, no hay alumnos registrados, por favor seleccione opción 1.")
    else:
        for nombre in diccionario_a:
            print(f"Nombre alumno: {nombre}. Notas: {diccionario_a[nombre]}") # dicionario_a[nombre] muestra la lista


# 3 función ver promedios:

# 4 función mejor alumno:

# 5 funcion cantidad de aprobados:

# 6 función sacar promedios:

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
            agregar_alumno(diccionario_a)
        case 2:
            mostrar_alumnos(diccionario_a)
        case 3:
            ver_promedios(diccionario_a)
        case 4:
            mejor_alumno(diccionario_a)
        case 5:
            cantidad_aprobados(diccionario_a)
        case 6:
            print("Saliendo...")
            break
        case _:
            print("Error, debe seleccionar una opción del 1 al 6.")