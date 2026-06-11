# funciones para ej2-2.py

# 1 función agregar alumno:
def agregar_alumno(diccionario_a):

    while True:
        nombre = input("Ingrese el nombre del alumno: ")
        if (nombre == "") or (nombre in diccionario_a):
            print("Error, el nombre no puede estar vacío ni repetirse con uno ya existente.")
        else:
            print("Nombre ingresado con éxito.")
            break
    
    while True:
        try:
            notas_ingresar = int(input("Ingrese la cantidad de notas a registrar: "))
            if (notas_ingresar > 0):
                print(f"Éxito. Usted registrará {notas_ingresar} notas.")
                break
            else:
                print("Error, debe registrar al menos una nota.")
        except ValueError:
            print("Error, el valor debe ser numérico, sin decimales ni letras.")

    lista_notas = []
    for i in range(notas_ingresar): # usa range porque notas_ingresar no es iterable (es solo 1 numero).
        cada_nota = validar_cada_nota() # esta funcion tira una nota por cada vuelta del for.
        lista_notas.append(cada_nota) # como hice la validacion en una funcion aparte, si algo sale
                                      # mal en curso, se terminará la funcion de cada nota pero no se 
                                      # terminará el ingreso de notas acá, sino que queda inconcluso y el for sigue.

    diccionario_a[nombre] = lista_notas # no usar corchetes en [lista_notas] sino agrega doble corchetes a la lista

# funcion para validar cada_nota en funcion agregar_alumno:
def validar_cada_nota():

    while True:
        try:
            nota = float(input(f"Ingrese la nota: "))
            if (nota >= 1) and (nota <= 7):
                print("Ingreso exitoso.")
                return nota # acá termina la funcion pero el for de la otra funcion hará que se repita esto,
                            # return nota hace que el resultado de esta funcion sea entregar 1 nota hacia la
                            # variable cada_nota y como allá arriba se repite en un for, validará nota por nota,
                            # no es necesario un break porque el return termina la función y el ciclo.
            else:
                print("Error. La nota debe ser entre 1 y 7.")
        except ValueError:
            print("Error, la nota debe ser un valor numérico.")

# 2 función mostrar alumnos:
def mostrar_alumnos(diccionario_a):

    if len(diccionario_a) == 0:   # diccionario vacío, usar len()
        print("Error, no hay alumnos registrados, por favor seleccione opción 1.")
        return # termina la función, vuelve al menú
    
    for nombre in diccionario_a:
        print(f"Nombre alumno: {nombre}. Notas: {diccionario_a[nombre]}") # dicionario_a[nombre] muestra la lista

# 3 función ver promedios:
def ver_promedios(diccionario_a):

    if len(diccionario_a) == 0:
        print("Error, no hay alumnos registrados, por favor seleccione opción 1.")
        return
    
    for nombre in diccionario_a:
        promedio = sum(diccionario_a[nombre]) / len(diccionario_a[nombre])
        print(f"Alumno: {nombre}. Promedio: {promedio:.1f}.")

# 4 función mejor alumno:
def mejor_alumno(diccionario_a):

    if len(diccionario_a) == 0:
        print("Error, no hay alumnos registrados, por favor seleccione opción 1.")
        return
    
    mejor_promedio = 0
    mejor_nombre = ""
    for nombre in diccionario_a:
        promedio = sum(diccionario_a[nombre]) / len(diccionario_a[nombre])
        if promedio > mejor_promedio:
            mejor_promedio = promedio
            mejor_nombre = nombre
    print(f"Mejor alumno: {mejor_nombre}. Promedio de {mejor_nombre}: {mejor_promedio:.1f}")

# 5 funcion cantidad de aprobados:
def cantidad_aprobados(diccionario_a):

    if len(diccionario_a) == 0:
        print("Error, no hay alumnos registrados, por favor seleccione opción 1.")
        return
    
    aprobados = 0
    for nombre in diccionario_a:
        promedio = sum(diccionario_a[nombre]) / len(diccionario_a[nombre])
        if promedio >= 4:
            aprobados = aprobados + 1
    print(f"Cantidad de alumnos aprobados: {aprobados}.")