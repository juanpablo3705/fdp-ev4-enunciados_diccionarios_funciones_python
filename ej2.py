# crear diccionario vacio:
diccionario_alumnos = {}

# 1 funcion agregar alumnos con sus notas:
def agregar_alumno(diccionario_alumnos):
    nombre_a_agregar = input("Ingrese el nombre del alumno: ")
    notas_a_ingresar = int(input("Ingrese la cantidad de notas a registrar: "))
    lista_notas = [] # creo una lista vacia antes de agregar las notas al diccionario
    for i in range(notas_a_ingresar):
        nota = float(input(f"Ingrese la nota numero {i + 1} de {notas_a_ingresar} de {nombre_a_agregar}: "))
        print(f"Nota {nota:.2f} registrada.")
        lista_notas.append(nota) # agrego cada nota a la lista, temporalmente
    diccionario_alumnos[nombre_a_agregar] = lista_notas # recogo la lista completa lista_notas y la añado al diccionario permanentemente

# 2 funcion mostrar alumnos y sus notas:
def mostrar_alumnos(diccionario_alumnos):
    for cada_nombre in diccionario_alumnos:
        print(f"Nombre: {cada_nombre}. Notas: {diccionario_alumnos[cada_nombre]}.")

# 3 funcion ver promedios:
def ver_promedios(diccionario_alumnos):
    for cada_nombre in diccionario_alumnos:
        lista_notas = diccionario_alumnos[cada_nombre] # creo una lista solo con los valores o notas de cada clave
        suma_notas = 0
        cantidad_notas = 0
        for cada_nota in lista_notas: # proceso sumar y contar notas de la lista lista_notas. cada_nota significa cada nota de la lista
            suma_notas = suma_notas + cada_nota
            cantidad_notas = cantidad_notas + 1
        promedio = suma_notas / cantidad_notas # si ya tengo la suma y el conteo, puedo sacar promedio
        print(f"Alumno: {cada_nombre}. Promedio: {promedio:.2f}.")

# 4 funcion mejor alumno:
def mejor_alumno(diccionario_alumnos):
    mejor_nombre = ""
    mejor_promedio = 0
    for cada_nombre in diccionario_alumnos:
        lista_notas = diccionario_alumnos[cada_nombre]
        suma_notas = 0
        cantidad_notas = 0
        for cada_nota in lista_notas:
            suma_notas = suma_notas + cada_nota
            cantidad_notas = cantidad_notas + 1
        promedio = suma_notas / cantidad_notas
        if promedio > mejor_promedio:
            mejor_promedio = promedio
            mejor_nombre = cada_nombre
    print(f"Mejor promedio: {mejor_promedio:.2f} del alumno: {mejor_nombre}.")

# 5 funcion cantidad de aprobados:
def cantidad_aprobados(diccionario_alumnos):
    alumnos_aprobados = 0
    for cada_alumno in diccionario_alumnos:
        lista_notas = diccionario_alumnos[cada_alumno]
        suma_notas = 0
        cantidad_notas = 0
        for cada_nota in lista_notas:
            suma_notas = suma_notas + cada_nota
            cantidad_notas = cantidad_notas + 1
        promedio = suma_notas / cantidad_notas
        if promedio >= 4:
            alumnos_aprobados = alumnos_aprobados + 1
    print(f"Cantidad alumnos aprobados: {alumnos_aprobados}.")

# menú programa principal:
while True:
    print("----- Menú -----")
    print("1. Agregar alumno con sus notas")
    print("2. Mostrar alumnos y sus notas")
    print("3. Ver promedios")
    print("4. Mejor alumno")
    print("5. Cantidad de aprobados")
    print("6. Salir")

    opcion_menu = int(input("Ingrese una opción del menú: "))

    match opcion_menu:
        case 1:
            agregar_alumno(diccionario_alumnos)
        case 2:
            mostrar_alumnos(diccionario_alumnos)
        case 3:
            ver_promedios(diccionario_alumnos)
        case 4:
            mejor_alumno(diccionario_alumnos)
        case 5:
            cantidad_aprobados(diccionario_alumnos)
        case 6:
            print("Saliendo...")
            break
        case _:
            print("Error. Debe ingresar una opción del 1 al 6.")